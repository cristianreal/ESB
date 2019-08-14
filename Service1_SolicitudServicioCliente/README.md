# Solicitud de servicio por parte del cliente

### SERVICIO 1

##### IMPORTANTE:
Este servicio se encuentra alojado en el puerto 8050

### Desarrollo del problema:
Para este primer servicio el CLI interactua con el ESB que realiza una peticion hacia el servicio de solicitud que luego vuelve a interactuar con el ESB para que se le notifique al servicio que representa al piloto.

### Solucion:
Para esta solicion se implementaron los siguientes procedimientos:

|No.|Ruta|Tipo|Parametros||
|--|----|:--:|:--------:|--------------------------|
|1|/SolicitudCliente|GET|Nombre, Correo, Ubicacion|https://host:8050/SolicitudCliente?Nombre=Name1&Correo=Email1&Ubicacion=Address|
|2|-|-|-|-|

A continuacion se describen los 3 parametros de la ruta /SolicitudCliente:
  1)  Nombre: De quien solicita el servicio.
  2)  Correo: Para comunicarnos con quien solicita el servicio.
  3)  Ubicacion: Para notificar a los pilotos el destino al que debe recoger a quien solicita el servicio.
  4)  Obligatorio: Enviar tres parametros a la ruta en el orden descrito de lo contrario mostrara un mensaje de error.

---
![](Images/IMG6.jpg)
