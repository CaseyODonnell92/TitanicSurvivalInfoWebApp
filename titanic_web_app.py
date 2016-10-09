from flask import Flask
from flask import render_template
import titanic_data
import json

app = Flask(__name__)

@app.route('/')
def titanic_stats():
	data = titanic_data.get_titanic_data()
	num_passengers = len(data)
	survivors = []
	deceased = []

	#populate lists of deceased and survivors
	while len(data) > 0:
		if data[0]['survived'] == "0":
			deceased.append(data.pop(0))
		else:
			survivors.append(data.pop(0))

	return render_template('titanic_template.html', num_passengers = num_passengers, 
													num_survivors = len(survivors), 
													num_deceased=len(deceased),
													survAge = json.dumps(titanic_data.get_age_categories(survivors)),
													survSex = json.dumps(titanic_data.get_gender(survivors)),
													survClass = json.dumps(titanic_data.get_class(survivors)),
													nonSurvAge = json.dumps(titanic_data.get_age_categories(deceased)),
													nonSurvSex = json.dumps(titanic_data.get_gender(deceased)),
													nonSurvClass = json.dumps(titanic_data.get_class(deceased)))