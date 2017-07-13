using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;


namespace Nico.Hubs
{
    using Microsoft.AspNet.SignalR;
    public class MyHub : Hub
    {
        public static void Answer()
        {
            IHubContext hubContext = GlobalHost.ConnectionManager.GetHubContext<MyHub>();
            if (hubContext != null)
            {
                hubContext.Clients.All.nicoAnswer();
            }
        }

        

    }
}