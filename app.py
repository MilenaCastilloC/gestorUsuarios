from flask import request
from flask_restful import Resource,Api
from flask import Flask
from typing import Dict
from flask import Flask
from urllib.error import HTTPError
from datetime import datetime
import requests

def create_app(config_dict: Dict = {}):
    app = Flask(__name__)    
    return app

seguridad = "http://miso-gestorseguridad.herokuapp.com/gestorSeguridad/authenticateUser"
def validarAccion(user_name, u_password):
    response = requests.post(seguridad+'/authenticateUser', json={"username": user_name, "password": u_password})
    if response.status_code == 200:
        data = response.json()
        return data
    else: 
        return False

class VistaSignIn(Resource):
    
    def get(self):
            autoriza = validarAccion('user_name', 'u_password')
            if autoriza== False:
                return {'mensaje':'Nombre de usuario o password incorrectos'}, 400
            else:
                return {'mensaje':'Inicio de sesión exitoso'}, 200

class HealthCheck(Resource):    

    def get(self):
        data={
            "echo" : "ok"
        }
        return data

app = create_app()
app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(VistaSignIn, "/signin")
api.add_resource(HealthCheck, "/signin/healtcheck")

if __name__ == '__main__':
    app.run()
