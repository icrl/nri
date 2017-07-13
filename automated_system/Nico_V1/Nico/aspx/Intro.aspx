<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Intro.aspx.cs" Inherits="Nico.aspx.Intro" %>



<asp:Content ID="Content1" ContentPlaceHolderID="MainContent" runat="server">


    
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <div class="container">
        <br />

        <h3> Instructions</h3>
        <h4> You will be teaching Nico how to solve the problems on the next page. To talk to Nico, press the spacebar. When you are done talking,
            release the spacebar and wait for Nico to respond. To go to the next problem, click on the text labeled 'Next.' When you reach the last problem,
            you will see a page that says 'Thank you, you are all done!'. Inform the experimenter when you reach this page.  
        </h4>

        <br />
        <div style="text-align:center;">
          <h4><asp:LinkButton ID="GoToProblemOne" Text="Start Teaching"  OnClick="Start_Teaching" runat="server" style="color:hsl(0, 0%, 30%)"/></h4>
        </div>
        <br />
    </div>

</asp:Content>



