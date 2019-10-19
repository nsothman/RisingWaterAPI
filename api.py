from flask import request, Flask
from flask_restful import Resource, Api
import pandas as pd

app = Flask(__name__)
api = Api(app)

class main(Resource):
    def post(self):
        data = pd.read_csv('Final_data.csv')
        date = request.get_json()
        i = 0
        while(float((date['date'])) >= float(data['Time'][i])):
            GMSL = float(data['Mean Value'][i])
            i += 1
        return {'GMSL': GMSL}

api.add_resource(main, '/')
app.run(debug = True)
