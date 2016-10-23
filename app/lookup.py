import csv
import string

def lookup(item_name):
	with open('test.csv', 'rb') as csvfile:
		csvreader = csv.reader(csvfile)
		for row in csvreader:
			if row[1].lower() == item_name.lower():
				return float(row[4])
		return -1