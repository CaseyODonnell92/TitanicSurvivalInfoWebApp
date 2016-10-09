# TitanicSurvivalInfoWebApp

Author: Casey O'Donnell

Setup:
In order to run titanic\_web_app.py, you need to set up a python virtual environment
within the project directory. Within this virtual environment, you then need to install
Flask and Requests (pip install flask requests).

Once this has been set up, execute export FLASK\_APP=titanic\_web_app.py.
To run the application, execute python -m flask run. The server will then
listen to requests on port 5000. To make the application respond to external
requests, execute python -m flask run --host=0.0.0.0