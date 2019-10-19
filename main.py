from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
import datetime

app = Flask(__name__)
api = Api(app)

data = pd.read_csv('data.csv')

class main(Resource):
    def get(self):
        #TASK1 get the time request
        date = request.args.get('date')
        if(date):
        #TASK2 compare the time in the request with data
            i = 0
            while(date >= datetime.strptime(data.get('Time'), '%Y-%M-%D')):
                GMSL = data.get('GMSL')[i]
                i+=1
        #TASK3 return the GMSL
            return {'GMSL': GMSL}

api.add_resource(main, '/')

if __name__ == '__main__':
    app.run(debug = True)
