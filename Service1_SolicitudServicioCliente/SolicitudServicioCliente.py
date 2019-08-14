"""
Para crear nuestro servicio es escencial importar las librerias de Flask, render_template, request, Response
"""
import requests
from flask import Flask, render_template, request, Response

app = Flask(__name__)

"""
    Se define la clase que contendra los metodos de nuestro servicio de Solicitud de Clientes.
    Importante:
    Todos los metodos de las clases deben de tener como parametro el "self", que es como el .this en Java
"""
class WS1_SolicitudCliente():
    """
    La funcion __init__ sera el constructor de la clase [WS1_SolicitudCliente], que se utilizara cuando se cree un objeto de de esta misma.
    Esta clase tendra tres atributos Ubicacion, Correo, Nombre
    """
    def __init__(self, Ubicacion, Correo, Nombre):
        self.Ubicacion = Ubicacion
        self.Correo = Correo
        self.Nombre = Nombre

"""
    La ruta https://host:8050/SolicitudCliente es de tipo GET que espera 3 parametros que se describen a continuacion:

    1)  Nombre: De quien solicita el servicio.
    2)  Correo: Para comunicarnos con quien solicita el servicio.
    3)  Ubicacion: Para notificar a los pilotos el destino al que debe recoger a quien solicita el servicio.

    La forma de acceder a esta ruta es la siguiente:
    https://host:8050/SolicitudCliente?Nombre=Name1&Correo=Email1&Ubicacion=Avenue%205%20Zone%205
    
    De forma obligatoria deben de ingresar los tres parametros de lo contrario mostrara un mensaje de error.
    
    Este servicio enviara la solicitud del servicio y esperara que algun piloto le responda para que sepa que ya fue tomado en cuenta
"""
@app.route('/SolicitudCliente', methods=['GET'])
def SolicitudCliente():
    nombre = request.args.get('Nombre')
    correo = request.args.get('Correo')
    ubicacion = request.args.get('Ubicacion')
    if nombre == '' or correo == '' or ubicacion == '':
        return '[SolicitudCliente]Parametros incompletos'
    response = requests.get('http://127.0.0.1:8080/SolicitudServicio', params={'Nombre': nombre, 'Correo': correo,'Ubicacion': ubicacion})
    print(response.content)
    return response.content

"""
    a continuacion se define que nuestro servicio se desplegara en el puerto 8050, la razon de utilizar un puerto diferente
    al predeterminado, se debe a que tenemos 3 servicios servicios diferentes y cada uno se debe ejecutar en un puerto diferente al resto.
"""    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8050)