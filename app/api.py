
# api for restful access
from flask import Flask, render_template
from flask_restful import Resource, Api
from sqlalchemy import create_engine
# from json import dumps


e = create_engine('sqlite:////home/thebadger2017/houseofpi/houseofpi/app/db/suntimes.sdb')

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)


@app.route('/')

def hello():
	user = { 'nickname': 'Peter' }
	return render_template('index.html',
				title='Welcome to HouseOfPi',
				user=user)



class Suntime_List(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from suntimes")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'devices': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient

class Statuses_List(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from status")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'statuses': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class Devices_List(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from devices")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'devices': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class multiply(Resource):
    '''dummy function to test apis'''
    def get(self, number):  # param must match uri identifier
        return number * 2

api.add_resource(Suntime_List, '/suntimes')
api.add_resource(Statuses_List, '/status')
api.add_resource(Devices_List, '/devices')
api.add_resource(multiply, '/multiply/<int:number>')  # whatever the number is, multiply by 2

if __name__ == '__main__':
     app.run()

