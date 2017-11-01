using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;


namespace Nico.Hubs
{
    using Microsoft.AspNet.SignalR;
    public class MyHub : Hub
    {
        public static void Start()
        {
            IHubContext hubContext = GlobalHost.ConnectionManager.GetHubContext<MyHub>();
            if (hubContext != null)
            {
                hubContext.Clients.All.startRecord();
            }
        }

        public static void Stop()
        {
            IHubContext hubContext = GlobalHost.ConnectionManager.GetHubContext<MyHub>();
            if (hubContext != null)
            {
                hubContext.Clients.All.stopRecord();
            }
        }

        public static void Play()
        {
            IHubContext hubContext = GlobalHost.ConnectionManager.GetHubContext<MyHub>();
            if (hubContext != null)
            {
                hubContext.Clients.All.playM();
            }
        }

        public static void PlayStep()
        {
            IHubContext hubContext = GlobalHost.ConnectionManager.GetHubContext<MyHub>();
            if (hubContext != null)
            {
                hubContext.Clients.All.playS();
            }
        }

    }
}