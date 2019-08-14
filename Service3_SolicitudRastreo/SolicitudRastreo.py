"""
Para crear nuestro servicio es escencial importar las librerias de Flask, render_template, request, Response
"""
import requests
from flask import Flask, render_template, request, Response
app = Flask(__name__)

"""
    Se define la clase que contendra los metodos de nuestro servicio de Solicitud de Rastreo.
    Importante:
    Todos los metodos de las clases deben de tener como parametro el "self", que es como el .this en Java
"""
class WS3_SolicitudRastreo():
    """
    La funcion __init__ sera el constructor de la clase [WS3_SolicitudRastreo], que se utilizara cuando se cree un objeto de de esta misma.
    Esta clase tendra tres atributos Ubicacion
    """
    def __init__(self, Ubicacion):
        self.Ubicacion = Ubicacion

"""
    La ruta https://host:8070/RastreoPiloto es de tipo GET que espera 1 parametro que se describe a continuacion:

    1)  Ubicacion: Yes|No.

    La forma de acceder a esta ruta es la siguiente:
    https://host:8070/RastreoPiloto?Ubicacion=[Yes|No]

    Este servicio servira para notificar a la administracion la ubicacion del piloto.

    De forma obligatoria deben de ingresar el parametro de lo contrario mostrara un mensaje de error.
"""
@app.route('/RastreoPiloto', methods=['GET'])
def RastreoPiloto():
    mensaje = request.args.get('Ubicacion')
    if mensaje == 'yes':
        response = requests.get('http://127.0.0.1:8080/SolicitudUbicacion', params={'Ubicacion': mensaje})
        return response.content
    return '[RastreoPiloto]Solicitud de rastreo Invalida'

"""
    a continuacion se define que nuestro servicio se desplegara en el puerto 8060, la razon de utilizar un puerto diferente
    al predeterminado, se debe a que tenemos 3 servicios servicios diferentes y cada uno se debe ejecutar en un puerto diferente al resto.
"""    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8070)