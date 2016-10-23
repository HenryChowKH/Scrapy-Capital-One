from flask import render_template, request, redirect
from app import app

import requests
import json
import datetime

from lookup import lookup

from app.utils import format_price

from enum import Enum

# move this to a config file that will not be included in the repo
apiKey = app.config["API_KEY"] # get the API Key from the config file

# http://www.davidadamojr.com/handling-cors-requests-in-flask-restful-apis/
@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
	return response

# Home page route. Loads the accounts.
@app.route('/')
@app.route('/index')
def index():
	# create the URL for the request
	accountsUrl = 'http://api.reimaginebanking.com/accounts?key={}'.format(apiKey)

	# make call to the Nessie Accounts endpoint
	accountsResponse = requests.get(accountsUrl)
	
	# if the accounts call responds with success
	if accountsResponse.status_code == 200:
		accounts = json.loads(accountsResponse.text)

		# filter out any credit card accounts (can't transfer money to/from them)
		accountsNoCards = []
		for account in accounts:
			if account["type"] != "Credit Card":
				accountsNoCards.append(account);

		# variable which will keep track of all transfers to pass to UI
		transfers = []
		
		# for each account make a request to get it's transfers where it is the payer only...
		for account in accounts:
			transfersUrl = 'http://api.reimaginebanking.com/accounts/{}/transfers?type=payer&key={}'.format(account['_id'], apiKey)
			transfersResponse = requests.get(transfersUrl)

			# if the transfer GET request was successful, add the resulting transfers to the array of data
			if transfersResponse.status_code == 200:
				transfers.extend(json.loads(transfersResponse.text))

		return render_template("home.html", accounts=accounts, format_price=format_price, transfers=transfers)
	else:
		return render_template("notfound.html")

# Banana route.
@app.route('/bananas')
def bananas():
	return render_template("homeBananas.html")

# Crawl route
@app.route('/crawl', methods=['POST'])
def crawl():
	crawled_item = request.form['item']

	# Look for the price of the crawled item
	price = lookup(crawled_item)

	# If non-existent
	if price < 0:
		return render_template("crawlResults.html", crawled_item='None')
	else:
		# Request balance
		url = "http://api.reimaginebanking.com/accounts/{}?key={}".format('580c020d360f81f104544e75', apiKey)
		response = requests.get(url)
		content = json.loads(response.text)
		balance = content['balance']
		# Calculate percentage
		percentage = 100. * price / float(balance)
		if percentage <= 20:
			color='green'
		elif percentage <= 50:
			color ='yellow'
		elif percentage <= 80:
			color = 'red'
		else:
			color = 'purple'
		return render_template("crawlResults.html", crawled_item=crawled_item, price=price,\
			percentage="%2.2f" % percentage, color=color)

# Transfer post route.  Makes request to Nessie API to create a transfer.
@app.route('/transfer', methods=['POST'])
def postTransfer():
	# toAccount = request.form["toAccount"]
	try:
		amount = float(request.form["amount"]) # need to convert to an int or this fails
	except ValueError:
		amount = ""
	
	if amount > 0:
		url = "http://api.reimaginebanking.com/accounts/{}/deposits?key={}".format('580c020d360f81f104544e75', apiKey)
	elif amount < 0:
		amount *= -1
		url = "http://api.reimaginebanking.com/accounts/{}/withdrawals?key={}".format('580c020d360f81f104544e75', apiKey)

	# set up payload for request
	body = {
		'medium' : "balance",
		'amount' : amount
	}

	# make the request to create the transfer
	response = requests.post(
		url,
		data=json.dumps(body),
		headers={'content-type':'application/json'})

	# redirect user to the same page, which should now show there latest transaction in the list
	return redirect("/index", code=302)