from flask import Flask
from flask import render_template
import titanic_data

app = Flask(__name__)

@app.route('/')
def hello_world():
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

	return render_template('titanic_template.html', num_passengers = num_passengers, \
													num_survivors = len(survivors), \
													num_deceased=len(deceased))