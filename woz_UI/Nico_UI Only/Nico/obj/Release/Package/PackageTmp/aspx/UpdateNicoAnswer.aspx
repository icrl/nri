<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="UpdateNicoAnswer.aspx.cs" Inherits="Nico.aspx.UpdateNicoAnswer" %>
<asp:Content ID="Content1" ContentPlaceHolderID="MainContent" runat="server">
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    
    <br />
    <br />
    <div>
        <div class="row">
            <div class="col-sm-4 text-center" >
                <button class="btn-primary" type="button" onclick="answer()">Fill in Answer for Current Problem and Step</button>
            </div>
        </div>
    </div>

    <div>
        <h2>Log</h2>
        <pre id="log"></pre>
    </div>

    <link rel="stylesheet" runat="server" media="screen" href="../content/bootstrap.css" />

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js" type="text/javascript"></script>
    <script src="https://code.jquery.com/jquery-1.9.1.min.js"></script>
    <script src="../js/jquery.signalR-2.0.0.min.js"></script>

    <script type="text/javascript">
  
        function answer() {

            //__log("Clicked button!");
            $.ajax({
                type: "POST",
                url: "UpdateNicoAnswer.aspx/fillAnswer",
                data: '{bitVar: "1"}',
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: OnSuccess,
                failure: function (response) {
                    alert(response.d);
                }
            });  
        }

        function OnSuccess(response) {
            __log("Answer trigger sent");
        }

        // function for writing data to window
        function __log(e, data) {
            log.innerHTML += "\n" + e + " " + (data || '');
        }
    </script>

</asp:Content>
