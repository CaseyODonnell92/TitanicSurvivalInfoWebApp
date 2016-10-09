import json
import requests

def get_titanic_data():
	response = requests.get("https://titanic.businessoptics.biz/survival/")
	results = json.loads(response.text)
	return results

def get_age_categories(list):
	age = {'unavailable': 0, '0-19':0, '20-39':0, '40-59':0, '60-79':0, '>80':0}
	for r in list:
		passenger_age = r['age']
		if passenger_age == '':
			age['unavailable'] += 1
			continue;
		else:
			passenger_age = eval(passenger_age)
		if passenger_age < 20:
			age['0-19'] += 1
		elif passenger_age < 40:
			age['20-39'] += 1
		elif passenger_age < 60:
			age['40-59'] += 1
		elif passenger_age < 80:
			age['60-79'] += 1
		else:
			age['>80'] += 1
	return age


def get_gender(list):
	'''Trigger Warning: cisnormativity ;)'''
	gender = {'male': 0, 'female': 0}
	for r in list:
		if r['sex'] == "male":
			gender['male'] += 1
		else:
			gender['female'] += 1
	return gender

def get_class(list):
	classes = {'First Class': 0, 'Second Class': 0, 'Third Class': 0}
	for r in list:
		if r['class'] == '1':
			classes['First Class'] += 1
		elif r['class'] == '2':
			classes['Second Class'] += 1
		elif r['class'] == '3':
			classes['Third Class'] += 1
	return classes

if __name__ == "__main__":
	results = get_titanic_data()
	survivors = []
	deceased = []
	passenger_count = len(results)

	while len(results) > 0:
		if results[0]['survived'] == "0":
			deceased.append(results.pop(0))
		else:
			survivors.append(results.pop(0))	

	print("There were " + str(passenger_count) + " passengers aboard the Titanic when it sank.")
	print("There were " + str(len(survivors)) + " survivors of the ship-wreck.")
	print(str(len(deceased)) + " people died in the wreck.")
	print("Survivor details:")
	print("Age break-down:")
	print(get_age_categories(survivors))
	print("Cabin class break-down:")
	print(get_class(survivors))
	print("Sex break-down:")
	print(get_gender(survivors))
	print("Non-Survivor details:")
	print("Age break-down:")
	print(get_age_categories(deceased))
	print("Cabin class break-down:")
	print(get_class(deceased))
	print("Sex break-down:")
	print(get_gender(deceased))
