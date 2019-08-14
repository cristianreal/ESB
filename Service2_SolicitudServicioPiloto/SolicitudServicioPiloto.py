"""
Para crear nuestro servicio es escencial importar las librerias de Flask, render_template, request, Response
"""

from flask import Flask, render_template, request, Response
app = Flask(__name__)

"""
    Se define la clase que contendra los metodos de nuestro servicio de Solicitud de Clientes.
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
    La ruta /SolicitudAvisoPiloto es de tipo GET que espera 3 parametros que se describen a continuacion:

    1)  Nombre: A quien se le prestara el servicio.
    2)  Correo: Para comunicarnos con quien solicita el servicio.
    3)  Ubicacion: Para dirigirnos a recogerla.

    La forma de acceder a esta ruta es la siguiente:
    /SolicitudAvisoPiloto?Nombre=Name1&Correo=Email1&Ubicacion=Address
    
    Este servicio servira para notificar al piloto sobre el viaje y que este le indique al solicitante que ya se dirige a su ubicacion.

    De forma obligatoria deben de ingresar los tres parametros de lo contrario mostrara un mensaje de error.
"""
@app.route('/SolicitudAvisoPiloto', methods=['GET'])
def basic1():
    nombre = request.args.get('Nombre')
    correo = request.args.get('Correo')
    ubicacion = request.args.get('Ubicacion')
    if nombre == '' or correo == '' or ubicacion == '':
        print('ERROR 400 - [SolicitudPiloto]Parametros incompletos')
        return 'ERROR 400 - [SolicitudPiloto]Parametros incompletos'
    print('Done 200 - Solicitud y Aviso Piloto: '+'Hola '+ nombre+'!!! Mi nombre es Juan Perez y sere su piloto para el viaje solicitado hacia: '+ ubicacion)
    return 'Done 200 - Solicitud y Aviso Piloto: '+'<br/>'+'Hola '+ nombre+'!!!'+'<br/>'+' Mi nombre es Juan Perez y sere su piloto para el viaje solicitado hacia: '+ ubicacion

"""
    a continuacion se define que nuestro servicio se desplegara en el puerto 8060, la razon de utilizar un puerto diferente
    al predeterminado, se debe a que tenemos 3 servicios servicios diferentes y cada uno se debe ejecutar en un puerto diferente al resto.
"""    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8060)