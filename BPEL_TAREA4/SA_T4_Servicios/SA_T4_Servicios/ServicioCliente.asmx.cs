using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;

namespace SA_T4_Servicios
{
    /// <summary>
    /// Descripción breve de ServicioCliente
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // Para permitir que se llame a este servicio web desde un script, usando ASP.NET AJAX, quite la marca de comentario de la línea siguiente. 
    // [System.Web.Script.Services.ScriptService]
    public class ServicioCliente : System.Web.Services.WebService
    {

        [WebMethod]
        public String SolicitudCliente(String Nombre, String Correo, String Ubicacion)
        {

            //PRIMER PASO   [ENDPOINT]
            //SEGUNDO PASO  [SOAPACTION] NAMESPACE / PROCESS
            //TERCER PASO   [XMLCONTENT]
            String mensaje = Comunicacion.InvokeService(
                @"http://localhost:8080/ode/processes/ClienteProceso", 
                @"SOAPAction:http://ClienteProceso.localhost/process", 
                @"<soapenv:Envelope xmlns:soapenv=""http://schemas.xmlsoap.org/soap/envelope/"" xmlns:q0=""http://ClienteProceso.localhost"" xmlns:xsd=""http://www.w3.org/2001/XMLSchema"" xmlns:xsi=""http://www.w3.org/2001/XMLSchema-instance"" >
            <soapenv:Header>   
            </soapenv:Header>
            <soapenv:Body>  
                <q0:ClienteProcesoRequest>
                    <q0:Nombre>"+Nombre+@"</q0:Nombre>
                    <q0:Correo>"+Correo+@"</q0:Correo>
                    <q0:Ubicacion>"+Ubicacion+@"</q0:Ubicacion>
                </q0:ClienteProcesoRequest>
            </soapenv:Body>  
            </soapenv:Envelope>");
            return mensaje;
        }

    }
}
