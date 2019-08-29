using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;

namespace SA_T4_Servicios
{
    /// <summary>
    /// Descripción breve de ServicioRastreo
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // Para permitir que se llame a este servicio web desde un script, usando ASP.NET AJAX, quite la marca de comentario de la línea siguiente. 
    // [System.Web.Script.Services.ScriptService]
    public class ServicioRastreo : System.Web.Services.WebService
    {

        [WebMethod]
        public string RastreoPiloto(String informar)
        {
            if (informar.Equals(""))
            {
                return "[RastreoPiloto]Solicitud de rastreo Invalida";
            }
            //PRIMER PASO   [ENDPOINT]
            //SEGUNDO PASO  [SOAPACTION] NAMESPACE / PROCESS
            //TERCER PASO   [XMLCONTENT]
            String mensaje = Comunicacion.InvokeService(
                @"http://localhost:8080/ode/processes/RastreoProceso",
                @"SOAPAction:http://RastreoProceso.localhost/process",
                @"<soapenv:Envelope xmlns:soapenv=""http://schemas.xmlsoap.org/soap/envelope/"" xmlns:q0=""http://RastreoProceso.localhost"" xmlns:xsd=""http://www.w3.org/2001/XMLSchema"" xmlns:xsi=""http://www.w3.org/2001/XMLSchema-instance"" >
            <soapenv:Header>   
            </soapenv:Header>
            <soapenv:Body>  
                <q0:RastreoProcesoRequest>
                  <q0:input>"+informar+@"</q0:input>
                </q0:RastreoProcesoRequest>
            </soapenv:Body>  
            </soapenv:Envelope>");
            return mensaje;
        }
    }
}
