<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Intro.aspx.cs" Inherits="Nico.aspx.Intro" %>



<asp:Content ID="Content1" ContentPlaceHolderID="MainContent" runat="server">


    
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <div class="container">
        <br />
        <h3> Introduction Video </h3>
        <video  width="960" height="540" controls>
                <source src="../content/video/introductionVideo.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <br />
        <div style="text-align:center;">
            <h4><asp:LinkButton ID="GoToHelloNico" Text="Click Here to Say Hello to Nico"  OnClick="Hello_Nico" runat="server" style="color:hsl(0, 0%, 30%)"/></h4>
        </div>
        <br />
    </div>

</asp:Content>



