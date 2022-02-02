# Python program to read
# json file


import json

# Opening JSON file
f = open('data.json',)

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['emp_details']:
	for k in i :
		if k == 'pin':
			print(i['emp_name'])


# Closing file
f.close()
