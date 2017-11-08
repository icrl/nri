using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Data;
using System.Data.SqlClient;
using System.Configuration;
using System.Text;

namespace Nico.csharp.functions
{
    public class SQLConditionGenderInfo
    {

        public string UserID { get; set; }
        public string Condition { get; set; }
        public string Gender { get; set; }
        public string RobotIP { get; set; }

        public static void UpdateConditionGender(string userid, string condition, string gender, string robotip)
        {
            try
            {
                string connectionString = null;
                SqlConnection connection;
                SqlDataAdapter adapter = new SqlDataAdapter();
                string sql = null;
                connectionString = ConfigurationManager.ConnectionStrings["NicoDB"].ConnectionString;
                connection = new SqlConnection(connectionString);
                sql = "UPDATE NicoDB.dbo.USERS SET Condition = @Condition, Gender = @Gender, RobotIP = @RobotIP WHERE NicoDB.dbo.USERS.UserID = @UserID";
                SqlCommand cmd = new SqlCommand(sql, connection);

                connection.Open();

                cmd.Parameters.AddWithValue("@UserID", userid);
                cmd.Parameters.AddWithValue("@Condition", condition);
                cmd.Parameters.AddWithValue("@Gender", gender);
                cmd.Parameters.AddWithValue("@RobotIP", robotip);
                cmd.ExecuteNonQuery();

                connection.Close();

            }
            catch (Exception error)
            {
                SQLLog.InsertLog(DateTime.Now, error.Message, error.ToString(), "SQLUpdateCondition UpdateGenderCondition", 0, userid);
            }
        }

        public static string GetCondition(string userid)
        {
            string queryString = "Select condition From NicoDB.dbo.USERS Where NicoDB.dbo.USERS.UserID = @UserID";
            string constr = ConfigurationManager.ConnectionStrings["NicoDB"].ConnectionString;
            string condition = "control";
            try
            {
                using (SqlConnection con = new SqlConnection(constr))
                {
                    SqlCommand cmd = new SqlCommand(queryString, con);
                    con.Open();
                    cmd.Parameters.AddWithValue("@UserID", userid);
                    condition = Convert.ToString(cmd.ExecuteScalar());
                }
            }
            catch (Exception error)
            {
                SQLLog.InsertLog(DateTime.Now, error.Message, error.ToString(), "SQLUpdateCondition GetCondition", 0, userid);
            }
            return condition;
        }

        public static string GetRobotIP(string userid)
        {
            string queryString = "Select robotIP From NicoDB.dbo.USERS Where NicoDB.dbo.USERS.UserID = @UserID";
            string constr = ConfigurationManager.ConnectionStrings["NicoDB"].ConnectionString;
            string robotIP = "192.168.1.8";
            try
            {
                using (SqlConnection con = new SqlConnection(constr))
                {
                    SqlCommand cmd = new SqlCommand(queryString, con);
                    con.Open();
                    cmd.Parameters.AddWithValue("@UserID", userid);
                    robotIP = Convert.ToString(cmd.ExecuteScalar());
                }
            }
            catch (Exception error)
            {
                SQLLog.InsertLog(DateTime.Now, error.Message, error.ToString(), "SQLUpdateCondition GetCondition", 0, userid);
            }
            return robotIP;
        }
    }
}