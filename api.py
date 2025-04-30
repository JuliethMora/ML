#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importación librerías
from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from m09_model_deployment_1 import predict_popularity

app = Flask(__name__)

# Cargar modelo al inicio para evitar recarga continua
reg = joblib.load('stack_model.pkl')


# Definición API Flask
api = Api(
    app, 
    version='1.0', 
    title='Song Popularity Prediction API',
    description='Predicts the popularity of a song based on audio features.'
)

ns = api.namespace('predict', description='popularity')

# Definición argumentos o parámetros de la API
parser = ns.parser()
parser.add_argument('danceability', type=float, required=True, help='Danceability score of the song', location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PopularityApi(Resource):

    @ns.doc(parser=parser)
    @ns.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        danceability = args['danceability']
        result = predict_popularity(danceability)
        return {"result": result}, 200
