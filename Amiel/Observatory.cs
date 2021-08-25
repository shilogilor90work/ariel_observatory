using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Amiel
{
    public class Observatory
    {
        public Observatory()
        {
            bool safe_or_not = safe();
        }

        public bool safe()
        {
            //url of api_status 
            var url = "http://18.222.50.25/api_status/ariel";
            var httpRequest = (HttpWebRequest)WebRequest.Create(url);

            httpRequest.Accept = "application/json";


            var httpResponse = (HttpWebResponse)httpRequest.GetResponse();
            using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
            {
                var result = streamReader.ReadToEnd();
                //if status is safe or not
                if (result.IndexOf("green") != -1)
                {
                    // status is safe to operate
                    safe_or_not = true;
                }
                else
                
                    // status is not safe to operate
                    safe_or_not = false;
                }
            }
            //return the status for ACP.weather
            return safe_or_not;

        }
    }
}
