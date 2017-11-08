<%@ Page Title="About" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="About.aspx.cs" Inherits="Nico.About" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
    <h3>About</h3>
    <p></p>

    <p>Set the gender and condition</p>

    <h4>Select Gender</h4>
    <select id="gender" name="selectGender">
        <option value="female">Female</option>
        <option value="male">Male</option>
    </select>

    <h4>Select Condition</h4>
    <select id="condition" name="selectCondition">
        <option value="control">Control</option>
        <option value="social">Social</option>
        <option value="entrain">Social and Entraining</option>
    </select>
    
    <h4>Input IP Address</h4>
    <input type="text" name="txtRobotIP" placeholder="192.168.1.8" id="robotIP" runat="server"/>
    <br />
    <h5>NOTE: Port number is 9559. This should not need to change. If you need to change it, see administrator.</h5>
    <br />
    <br />
    <asp:Button Text="Submit" runat="server" OnClick="Submit" />
    
</asp:Content>