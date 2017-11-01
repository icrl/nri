using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.IO;

namespace Nico.handlers
{
    /// <summary>
    /// Summary description for saveWav
    /// </summary>
    public class saveWav : IHttpHandler
    {

        public void ProcessRequest(HttpContext context)
        {
            string path1 = context.Request.PhysicalApplicationPath;
            using (StreamWriter ws = new StreamWriter(path1 + "data\\logs\\log_SaveWav.txt"))
            {

                try
                {


                    if (context.Request.Files.Count > 0)
                    {
                        HttpFileCollection files = context.Request.Files;
                        string path = context.Request.PhysicalApplicationPath;
                        string fullPath = "";
                        for (int i = 0; i < files.Count; i++)
                        {
                            HttpPostedFile file = files[i];
                            string username = "nlubold";
                            string formatFileName = string.Format("{0}-{1:yyyy-MM-dd_hh-mm-ss-tt}", file.FileName, DateTime.Now);
                            fullPath = path + "data\\userAudio\\" + username + "_" + formatFileName + ".wav";
                            file.SaveAs(fullPath);
                            fullPath = path + "data\\userAudio\\" + file.FileName + ".wav";
                            file.SaveAs(fullPath);
                        }


                        string transResponse = "Saved User Wav File!";

                        context.Response.ContentType = "audio/wav";
                        context.Response.AppendHeader("Access-Control-Allow-Origin", "*");
                        context.Response.AppendHeader("Access-Control-Allow-Headers", "x-requested-with");
                        context.Response.Write(transResponse);


                    }
                }
                catch (Exception error)
                {
                    ws.Write(error.Message);
                    ws.Write(error.StackTrace);

                }

            }
        }

        public bool IsReusable
        {
            get
            {
                return false;
            }
        }

    }
}