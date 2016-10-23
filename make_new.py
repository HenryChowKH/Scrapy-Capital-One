# Manually set some accounts

import requests
import json

key ='d91d900c5a04815aa481520b60b5840a'

url_stub = 'http://api.reimaginebanking.com'
url = url_stub + '/customers?key={}'.format(key)
# print(url)

# Create Bob Lob
# payload = {
#   "_id": '1',
#   "first_name": "Bob",
#   "last_name": "Lob",
#   "address": {
#     "street_number": "1337",
#     "street_name": "Highway 40",
#     "city": "Inner",
#     "state": "MA",
#     "zip": "H0HH0"
#   }
# }

# Create Account
# payload = {

#   "type": "Checking",
#   "nickname": "Purchasing Account",
#   "rewards": 0,
#   "balance": 10000
# }



# response = requests.get("http://api.reimaginebanking.com/accounts/580c020d360f81f104544e75?key={}".format(key))
# content = json.loads(response.text)
# balance = content['balance']
# new_balance = balance + amount

body = {
		'medium' : "balance",
		'amount' : 5
}

response = requests.post("http://api.reimaginebanking.com/accounts/{}/withdrawals?key={}".format('580c020d360f81f104544e75', key),
	data=json.dumps(body),
	headers={'content-type':'application/json'})
print(response)

# response = request.get('http://api.reimaginebanking.com/customers/580bd8e4360f81f104544dd3/accounts?key={}.format(key))
# response = requests.post(url_stub + '/customers/580bd8e4360f81f104544dd3/accounts?key={}'.format(key),
# 		data=json.dumps(payload),
# 		headers={'content-type':'application/json'}
# 	)
# print(response)
# print(response.text)


# response = requests.get(url_stub + '/customers?key={}'.format(key))
# accounts = json.loads(response.text)

# for account in accounts:
	# print(account)


# response = requests.post(
# 	url_stub + '/customers',
# 	data=json.dumps(payload),
# 	headers={'content-type':'application/json'}
# 	)


# Get customers
# response = requests.get(url)
# print(response.json())


# For each customer give an account
# print(response.json())


# for customer in response:
	# print (type(customer))
	# print (customer)
	# print(1)
	# requests.post(url_stub + '/customers/{}/accounts?key={}'.format(customer._id,key),
	# 	payload2)
# print(response.status_code)

# response = requests.post(
# 	url_stub + "/customers/1/accounts?key={}".format(key),
# 	data=json.dumps(payload),
# 	headers={'content-type':'application/json'}
# 	)
# print(response.status_code)
# print(response.json())


