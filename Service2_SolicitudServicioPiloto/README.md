# Recepcion de solicitud y aviso al piloto

### SERVICIO 2

##### IMPORTANTE:
Este servicio se encuentra alojado en el puerto 8060

### Desarrollo del problema:
Para este segundo servicio el CLI ya ha interactuado con el ESB quien realizo una peticion hacia el servicio de solicitud que luego vuelve a interactuar con el ESB para que se le notifique al servicio que representa al piloto y este ultimo pueda responder lo antes posible al cliente.

Este servicio servira para notificar al piloto sobre el viaje y que este le indique al solicitante que ya se dirige a su ubicacion.

### Solucion:
Para esta solicion se implementaron los siguientes procedimientos:

|No.|Ruta|Tipo|Parametros||
|--|----|:--:|:--------:|--------------------------|
|1|/SolicitudAvisoPiloto|GET|Nombre, Correo, Ubicacion|https://host:8050/SolicitudAvisoPiloto?Nombre=Name1&Correo=Email1&Ubicacion=Address|
|2|-|-|-|-|

A continuacion se describen los 3 parametros de la ruta /SolicitudAvisoPiloto:
  1)  Nombre: De quien solicita el servicio.
  2)  Correo: Para comunicarnos con quien solicita el servicio.
  3)  Ubicacion: Para notificar a los pilotos el destino al que debe recoger a quien solicita el servicio.
  4)  Obligatorio: Enviar tres parametros a la ruta en el orden descrito de lo contrario mostrara un mensaje de error.

---
![](Images/IMG7.jpg)
