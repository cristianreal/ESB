import requests
from flask import Flask, render_template, request, Response
app = Flask(__name__)

class ESB():
    def __init__(self, Nombre):
        self.Nombre = Nombre

@app.route('/', methods=['GET'])
def RastreoPiloto():
    nombre = request.args.get('Nombre')
    correo = request.args.get('Correo')
    ubicacion = request.args.get('Ubicacion')
    response = requests.get('http://127.0.0.1:8060/SolicitudAvisoPiloto', params={'Nombre': nombre, 'Correo': correo,'Ubicacion': ubicacion})
    return response.content

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)