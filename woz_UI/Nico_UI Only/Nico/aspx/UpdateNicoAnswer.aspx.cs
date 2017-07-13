using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using Nico.Hubs;

namespace Nico.aspx
{
    public partial class UpdateNicoAnswer : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        [System.Web.Services.WebMethod]
        public static string fillAnswer(string bitVar)
        {
            MyHub.Answer();
            return "Successful";
        }
    }
}