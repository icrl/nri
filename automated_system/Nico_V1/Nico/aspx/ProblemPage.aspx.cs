using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using Nico.csharp.functions;

/* 
 * On the page load, the problem table is populated. 
 * SQL calls provide the following information:
 *      The current problem and step
 *      The current answer pattern
 *      The data for the current problem (any associated text, images, and what goes in the table) 
 * If this is the first time to the page or we are revisiting from another page, Nico is triggered to speak through a page reload
 * If the user hasn't not spoken for some time, Nico is triggered to speak through a page reload
*/


/* Issues:
 *      Steps are off 
 *      Triggering dialouge behavior at every step move
 *      Bold isn't working (maybe because current step tracking is off??)
 *      Page also appears to be reloading twice though
*/

namespace Nico.aspx
{
    public partial class ProblemPage : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {





        }
        /*
        protected void Next_Problem(object sender, EventArgs e)
        {
            
            string userid = "nlubold";
            int sessionid = 1;
            int totalProblems = 2;

            List<int> problemStep = SQLProblemStepTracker.ReadProbStep(userid);                                      
            int problem = problemStep[0];
            int nextProblem = problem + 1;
            int problemImgKey = problemStep[2];
            int answerKey = 1;
            int step = 0;
            int newanswer = 0;

            // Variables important to Nico's state
            Tuple<string, int, bool> nicoResponse = new Tuple<string, int, bool>("", 0, false);                           // string => Nico's response, int is the movement code, second int is whether we update the problem step

            // Update user state & nico state
            DateTime now = DateTime.Now;
            string clickstep = "next problem";
            SQLUserState.UpdateSpeakerState(userid, "", "", 0, problemStep, now, clickstep);                            // Write out speaker state info
            SQLNicoState.UpdateNicoState(userid, nicoResponse, problemStep, now);                                       // Write out Nico's state info & update problem/step


            if (nextProblem > totalProblems)
            {
                Response.Redirect("../aspx/Default.aspx");
            }
            else
            {
                SQLProblemStepTracker.UpdateProbStep(userid, sessionid, nextProblem, step, problemImgKey, answerKey, newanswer);
                Response.Redirect("../aspx/ProblemPage.aspx");
            }
            

        }

        protected void NextStep_Click(object sender, EventArgs e)
        {
            
            string userid = "nlubold";
            int sessionid = 1;

            List<int> problemStep = SQLProblemStepTracker.ReadProbStep(userid);                                      // First two values indicate # of steps & # of cells
            int problem = problemStep[0];
            int step = problemStep[1];
            int nextStep = step + 1;
            int problemImgKey = problemStep[2];
            int answerKey = problemStep[3];
            int newanswer = 0;

            // update problem step to pass to Nico's response generator
            problemStep[1] = nextStep;

            // Variables important to Nico's state
            Tuple<string, int, bool> nicoResponse;                                                                      // string => Nico's response, int is the movement code, second int is whether we update the problem step
            string path = HttpRuntime.AppDomainAppPath;

            // Generate a response for Nico when move to the next step and update user state
            DateTime now = DateTime.Now;
            string clickstep = "next step";
            nicoResponse = ResponseGeneration.NicoResponse(path, problemStep, 0, "next step", now);
            SQLUserState.UpdateSpeakerState(userid, "", "", 0, problemStep, now, clickstep);                            // Write out speaker state info
            SQLNicoState.UpdateNicoState(userid, nicoResponse, problemStep, now);                                       // Write out Nico's state info & update problem/step

            // Update step on
            SQLProblemStepTracker.UpdateProbStep(userid, sessionid, problem, nextStep, problemImgKey, answerKey, newanswer);
            //Response.Redirect("../aspx/ProblemPage.aspx");
            
        }

        protected void PriorStep_Click(object sender, EventArgs e)
        {
            
            string userid = "nlubold";
            int sessionid = 1;

            List<int> problemStep = SQLProblemStepTracker.ReadProbStep(userid);                                      // First two values indicate # of steps & # of cells
            int problem = problemStep[0];
            int step = problemStep[1];
            int priorStep = step - 1;
            int problemImgKey = problemStep[2];
            int answerKey = problemStep[3];
            int newanswer = 0;

            // Variables important to Nico's state
            Tuple<string, int, bool> nicoResponse;                                                                      // string => Nico's response, int is the movement code, second int is whether we update the problem step
            string path = HttpRuntime.AppDomainAppPath;

            // Update problem step for generating Nico's response
            problemStep[1] = priorStep;

            // Generate a response for Nico when move to the next step and update user state
            DateTime now = DateTime.Now;
            string clickstep = "prior step";
            nicoResponse = ResponseGeneration.NicoResponse(path, problemStep, 0, "prior step", now);
            SQLUserState.UpdateSpeakerState(userid, "", "", 0, problemStep, now, clickstep);                            // Write out speaker state info
            SQLNicoState.UpdateNicoState(userid, nicoResponse, problemStep, now);                                       // Write out Nico's state info & update problem/step

            // Update step on
            SQLProblemStepTracker.UpdateProbStep(userid, sessionid, problem, priorStep, problemImgKey, answerKey, newanswer);
            Response.Redirect("../aspx/ProblemPage.aspx");
            
        }
        */
        override protected void OnInit(EventArgs e)
        {
            this.Load += new System.EventHandler(this.Page_Load);
        }
    }
}
