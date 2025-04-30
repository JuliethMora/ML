# Importación librerías
from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from m09_model_deployment_1 import predict_popularity

app = Flask(__name__)

# Definición API Flask
api = Api(
    app, 
    version='1.0', 
    title='popularity song Prediction API',
    description = 'popularity song Prediction API')

ns = api.namespace('predict', 
     description='popularity')

# Definición argumentos o parámetros de la API
parser = ns.parser()
parser.add_argument(
    'URL', 
    type=str, 
    required=True, 
    help='song to be analyzed', 
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
})

# Definición de la clase para disponibilización
@ns.route('/')
class PhishingApi(Resource):

    @ns.doc(parser=parser)
    @ns.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {
         "result": predict_popularity(args['URL'])
        }, 200
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)    
