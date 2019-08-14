"""
Para crear nuestro servicio es escencial importar las librerias de Flask, render_template, request, Response
"""
import requests
from flask import Flask, render_template, request, Response

app = Flask(__name__)

"""
    Se define la clase que contendra los metodos de nuestro servicio de Solicitud de Pilotos.
    Importante:
    Todos los metodos de las clases deben de tener como parametro el "self", que es como el .this en Java
"""
class WS2_SolicitudPiloto():
    """
    La funcion __init__ sera el constructor de la clase [WS2_SolicitudPiloto], que se utilizara cuando se cree un objeto de de esta misma.
    Esta clase tendra tres atributos Ubicacion, Correo, Nombre
    """
    def __init__(self, Ubicacion, Correo, Nombre):
        self.Ubicacion = Ubicacion
        self.Correo = Correo
        self.Nombre = Nombre






"""
    La ruta https://host:8060/SolicitudAvisoPiloto es de tipo GET que espera 3 parametros que se describen a continuacion:

    1)  Nombre: A quien se le prestara el servicio.
    2)  Correo: Para comunicarnos con quien solicita el servicio.
    3)  Ubicacion: Para dirigirnos a recogerla.

    La forma de acceder a esta ruta es la siguiente:
    https://host:8060/SolicitudAvisoPiloto?Nombre=Name1&Correo=Email1&Ubicacion=Address
    
    Este servicio servira para notificar al piloto sobre el viaje y que este le indique al solicitante que ya se dirige a su ubicacion.

    De forma obligatoria deben de ingresar los tres parametros de lo contrario mostrara un mensaje de error.

    Este servicio respondera al cliente para que se entere que ya fue tomado en cuenta
"""
@app.route('/SolicitudAvisoPiloto', methods=['GET'])
def SolicitudAvisoPiloto():
    nombre = request.args.get('Nombre')
    correo = request.args.get('Correo')
    ubicacion = request.args.get('Ubicacion')
    if nombre == '' or correo == '' or ubicacion == '':
        return '[Solicitud y Aviso Piloto]Parametros incompletos'
    return '[Solicitud y Aviso Piloto]: '+'Hola '+ nombre+'!!! Mi nombre es Ronaldinho Gaucho Perez y sere su piloto para el viaje solicitado hacia: '+ ubicacion






"""
    La ruta https://host:8060/UbicacionPiloto es de tipo GET que espera 1 parametro que se describe a continuacion:

    1)  Ubicacion: Yes|No.

    La forma de acceder a esta ruta es la siguiente:
    https://host:8060/UbicacionPiloto?Ubicacion=[Yes|No]

    Este servicio servira para notificar a la administracion la ubicacion del piloto.

    De forma obligatoria deben de ingresar el parametro de lo contrario mostrara un mensaje de error.
"""
@app.route('/UbicacionPiloto', methods=['GET'])
def UbicacionPiloto():
	mensaje = request.args.get('Ubicacion')
	if mensaje == 'yes':
		return '[UbicacionPiloto]Hola soy el piloto Ronaldinho Gaucho Perez y me encuentro en la siguiente direccion: '+'51°32\'01.4\'\'N 0°20\'37.5\'\'W'
	return '[UbicacionPiloto]Solicitud de rastreo Invalida'


    





"""
    a continuacion se define que nuestro servicio se desplegara en el puerto 8060, la razon de utilizar un puerto diferente
    al predeterminado, se debe a que tenemos 3 servicios servicios diferentes y cada uno se debe ejecutar en un puerto diferente al resto.
"""    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8060)