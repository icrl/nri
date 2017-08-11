using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Nico.csharp.functions;

namespace Nico.handlers
{
    /// <summary>
    /// Summary description for ErrorLogger
    /// </summary>
    public class ErrorLogger : IHttpHandler
    {

        public void ProcessRequest(HttpContext context)
        {
            try
            {
                string data = context.Request.Params["log"];    // Get transcript (if there is one)
                SQLLog.InsertLog(DateTime.Now,"From ProblemPage", data, "ErrorLogger.ashx.cs", 0, "nlubold");

            }
            catch(Exception error)
            {
                SQLLog.InsertLog(DateTime.Now, error.Message, error.ToString(), "ErrorLogger.ashx.cs", 0, "nlubold");
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