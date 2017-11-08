using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.IO;
using System.Web.Security;
using Nico.csharp.functions;


namespace Nico
{
    public partial class About : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
 
        }

        protected void Submit(object sender, EventArgs e)
        {
            string gender = Request.Form["selectGender"];
            string condition = Request.Form["selectCondition"];
            string path = Request.PhysicalApplicationPath;
            string userid = HttpContext.Current.User.Identity.Name;
            string robotAddress = robotIP.Value;
            try
            {
                SQLConditionGenderInfo.UpdateConditionGender(userid, condition, gender, robotAddress);
                Response.Redirect("default.aspx", false);
            }
            catch (Exception error)
            {
                SQLLog.InsertLog(DateTime.Now, error.Message, error.ToString(), "UpdateStep.ashx.cs", 0, userid);
            }

        }


    }
}