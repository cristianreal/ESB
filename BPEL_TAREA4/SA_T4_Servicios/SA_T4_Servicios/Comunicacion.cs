using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.IO;
using System.Net;
using System.Xml;

namespace SA_T4_Servicios
{
    public static class Comunicacion
    {
        public static HttpWebRequest CreateSOAPWebRequest(String Endpoint, String SOAPAction)
        {
            //Making Web Request    
            HttpWebRequest Req = (HttpWebRequest)WebRequest.Create(Endpoint);
            //SOAPAction    
            Req.Headers.Add(SOAPAction);
            //Content_type    
            //HTTP method    
            Req.Method = "POST";
            //return HttpWebRequest    
            return Req;
        }

        public static String InvokeService(String Endpoint, String SOAPAction, String xmlContent)
        {
            //Calling CreateSOAPWebRequest method    
            HttpWebRequest request = Comunicacion.CreateSOAPWebRequest(Endpoint, SOAPAction);

            XmlDocument SOAPReqBody = new XmlDocument();
            //SOAP Body Request    
            SOAPReqBody.LoadXml(xmlContent);



            using (Stream stream = request.GetRequestStream())
            {
                SOAPReqBody.Save(stream);
            }
            //Geting response from request    
            System.Diagnostics.Debug.WriteLine(request.ToString());
            try
            {
                using (WebResponse Serviceres = request.GetResponse())
                {
                    using (StreamReader rd = new StreamReader(Serviceres.GetResponseStream()))
                    {
                        //reading stream    
                        var ServiceResult = rd.ReadToEnd();
                        //writting stream result on console    
                        System.Diagnostics.Debug.WriteLine(ServiceResult);
                        System.Diagnostics.Debug.WriteLine("--------------------");
                        return ServiceResult;
                    }
                }
            }
            catch (WebException wex)
            {
                System.Text.StringBuilder sb = new System.Text.StringBuilder();
                sb.AppendLine("ERROR:" + wex.Message + ". STATUS: " + wex.Status.ToString());

                if (wex.Status == WebExceptionStatus.ProtocolError)
                {
                    var response = ((HttpWebResponse)wex.Response);
                    sb.AppendLine(string.Format("Status Code : {0}", response.StatusCode));
                    sb.AppendLine(string.Format("Status Description : {0}", response.StatusDescription));

                    try
                    {
                        StreamReader reader = new StreamReader(response.GetResponseStream());
                        sb.AppendLine(reader.ReadToEnd());
                    }
                    catch (WebException ex) { throw; }
                }

                throw new Exception(sb.ToString(), wex);
            }
            catch (Exception ex) { throw; }
            return "<ERROR>";
        }
    }
}