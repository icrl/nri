using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Nico.csharp.functions;

namespace Nico.handlers
{
    /// <summary>
    /// Summary description for UpdateAnswer
    /// </summary>
    public class UpdateAnswer : IHttpHandler
    {

        public void ProcessRequest(HttpContext context)
        {
            try
            {
                string userid = "nlubold";
                int sessionid = 1;
              
                List<int> problemStep = SQLProblemStepTracker.ReadProbStep(userid);
                int problem = problemStep[0];
                int nextproblem = problem + 1;
                int step = problemStep[1];
                int problemimgkey = problemStep[2];
                int answerKey = problemStep[3];
                int newanswer = problemStep[4];
                int numautoresponses = problemStep[5];
                int nextstepanswerkey = 0;
                int numAutoResponses = 0;
                
                if (step == 0)
                {
                    step = 1;
                }

                nextstepanswerkey = SQLProblemStepTracker.CalculateNewAnswerKey(1, answerKey, step);                
                newanswer = step;
                SQLProblemStepTracker.UpdateProbStep(userid, sessionid, problem, step, problemimgkey, nextstepanswerkey, newanswer, numAutoResponses);
            }
            catch (Exception error)
            {
                SQLLog.InsertLog(DateTime.Now, error.Message, error.ToString(), "UpdateAnswer.ashx.cs", 0, "nlubold");
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