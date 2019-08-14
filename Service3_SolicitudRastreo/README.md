# Solicitud de ubicacion (rastreo) desde la administración del servicio de carros

### SERVICIO 3

##### IMPORTANTE:
Este servicio se encuentra alojado en el puerto 8070

### Desarrollo del problema:
Este tercer servicio se encargara de notificar a la administracion la ubicacion del piloto para que luego por medio del ESB se pueda responder lo antes poisble.

Este servicio servira para notificar a la administracion sobre la ubicacion del piloto.

### Solucion:
Para esta solicion se implementaron los siguientes procedimientos:

 |No.|Ruta|Tipo|Parametros||
|--|----|:--:|:--------:|--------------------------|
|1|/RastreoPiloto|GET|Ubicacion|https://host:8070/RastreoPiloto?Ubicacion=Yes_No|
|2|-|-|-|-|

A continuacion se describen el parametro de la ruta /RastreoPiloto:
  1)  Ubicacion: [Yes|No].
  2)  Obligatorio: Enviar tres parametros a la ruta en el orden descrito de lo contrario mostrara un mensaje de error.

---
![](Images/IMG8.jpg)
