using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;

namespace SA_T4_Servicios
{
    /// <summary>
    /// Descripción breve de ServicioPiloto
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // Para permitir que se llame a este servicio web desde un script, usando ASP.NET AJAX, quite la marca de comentario de la línea siguiente. 
    // [System.Web.Script.Services.ScriptService]
    public class ServicioPiloto : System.Web.Services.WebService
    {

        [WebMethod]
        public string SolicitudAvisoPiloto(String Nombre, String Correo, String Ubicacion)
        {
            return "[Solicitud y Aviso Piloto]: " + 
                "Hola " + 
                Nombre + 
                "!!! Mi nombre es Ronaldinho Gaucho Perez y sere su piloto"+
                " para el viaje solicitado hacia: " + 
                Ubicacion;
        }

        [WebMethod]
        public string UbicacionPiloto(String informar)
        {
            if (informar.Equals(""))
            {
                return "[UbicacionPiloto]Solicitud de rastreo Invalida";
            }
            return "[UbicacionPiloto]Hola soy el piloto Ronaldinho Gaucho Perez "+
                "y me encuentro en la siguiente direccion: " +
                "51°32\'01.4\'\'N 0°20\'37.5\'\'W";
        }
    }
}
