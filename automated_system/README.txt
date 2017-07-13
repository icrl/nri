This code contains the architecture for the NRI project to run automatically with a NAO robot. To run this code, several steps need to be taken first in addition to installing Visual Studio Express. 

-------------------------------------------------

Setting up the Nao robot and chatbot APIs. 

(Assumption that this is being run on a Windows machine)

Step 1. Download Python 2.7
Step 2. Install Nao robot Python SDK (http://doc.aldebaran.com/1-14/dev/python/index.html)
Step 3. Install Pandora bot API (https://github.com/pandorabots/pb-python)
Step 4. Download the folder labeled NaoNRIPrograms and put this in C:\Python27\
Step 5. Open nico_move_speak.py and change the IP address to that of your Nao robot

-------------------------------------------------

Setting up the database (currently we are using a cloud-based MSSQL DB so this step is only if you want a local DB):

Step 1. Install MSSQL Server Express and use the NicoDB.bak file to restore a database called NicoDB from backup.
Step 2. Setup a SQL user to access the database (dbo role) under Security folder (general)
Step 3. Update web.config with name of local SQL server and user

Trouble-shooting for SQL user access: 
* Make sure Default DB set to NicoDB
* Under security in properties of the server, set to allow SQL Server Authentication and Windows Authentication
* Add port 1433 allowable through the Windows Firewall (advanced settings)
* Make sure SQL database is allowed through the Windows firewall
* Search for and open SQLServerManager13.msc (this is the configuration manager). From the configuration manager restart the server after each of the following changes: (a) From the configuration manager enable all protocols for SQLExpress under SQL server network configuration. (b) From the configuration manager under TCP/IP protocol change tcp ip port for IPAll to 1433. (c) From the configuration manager under TCP/IP protocol remove number of tcpip dynamic ports.
* In the web.config, set the server name to local 127.0.0.1

-------------------------------------------------

Once the above steps have been completed, open the project in Visual Studio Express and run it.
