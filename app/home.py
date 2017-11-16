
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')

@app.route('/index')
def hello():
	user = { 'nickname': 'Peter' }	
	return render_template('index.html', 
				title='Welcome to HouseOfPi',
				user=user)

