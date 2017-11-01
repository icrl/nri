using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.IO;
using Nico.csharp.functions;

namespace Nico.csharp.functions
{
    public class ResponseGeneration
    {
        /* Using speaker info, get Nico's response and instigate movement
         * Returns a tuple containing the path to the file of Nico's response, Nico's movement code, and whether Nico provided the answer to this step
        */
        public static Tuple<string, int, string> NicoResponse(string path, List<int> problemStep, int speakerSpoke, string transcript, DateTime time, string page, string userID, string useraudio)
        {

            Tuple<string, int, string> nicoResponse = new Tuple<string, int, string>("",1,"no answer");
            bool checkIfAnswered = false;

            try
            {
                // ****** IMPORTANT ******
                // These variables might change based on which NaoNRIProgram calling
                // File options:    C:\\Python27\\NaoNRIPrograms\\VerbalManager\\simpleGestureSelectionForAutomatedSys.py
                //                  C:\\Python27\\NaoNRIPrograms\\VerbalManager\\nonVerbalManager.py

                string verbalManagerFile = "C:\\Python27\\NaoNRIPrograms\\VerbalManager\\nonVerbalManager.py ";
                string condition = "entrain";

                // Get whether the current step has been answered and pass that along 
                int currentstep = problemStep[1];
                int answerKey = problemStep[3];
                int numturns = problemStep[6];
                string answerPattern = SQLAnswerPattern.GetAnswerPattern(answerKey)[1];
                char[] chAnswerPattern = answerPattern.ToCharArray();

                if (page == "ProblemPage")
                {

                    if (transcript == "" || transcript == null)                                                                                                          // Need to handle when there is no transcript - will depend on if this is the first time we've been here or not
                    {
                        //transcript = problemStep[0].ToString() + "_" + problemStep[1].ToString();
                        transcript = "no response";
                        nicoResponse = dialogueManager(path, problemStep, speakerSpoke, transcript, time, checkIfAnswered, condition);                                                                                      // Generate Nico's response (currently just pandorbots)
                        nicoMoveSpeak(nicoResponse.Item1, nicoResponse.Item2, verbalManagerFile, useraudio, condition, userID, time, numturns);
                    }
                    else if (transcript == "next step")
                    {
                        if (chAnswerPattern[currentstep + 1] == '1')
                        {
                            transcript = transcript + " " + problemStep[0].ToString() + " " + problemStep[1].ToString() + " a";
                        }
                        else
                        {
                            transcript = transcript + " " + problemStep[0].ToString() + " " + problemStep[1].ToString();
                        }
                        nicoResponse = dialogueManager(path, problemStep, speakerSpoke, transcript, time, checkIfAnswered, condition);                                                                                      // Generate Nico's response (currently just pandorbots)
                        nicoMoveSpeak(nicoResponse.Item1, nicoResponse.Item2, verbalManagerFile, useraudio, condition, userID, time, numturns);
                    }
                    else if (transcript == "prior step")
                    {
                        if (chAnswerPattern[currentstep - 1] == '1')
                        {
                            transcript = transcript + " " + problemStep[0].ToString() + " " + problemStep[1].ToString() + " a";
                        }
                        else
                        {
                            transcript = transcript + " " + problemStep[0].ToString() + " " + problemStep[1].ToString();
                        }

                        nicoResponse = dialogueManager(path, problemStep, speakerSpoke, transcript, time, checkIfAnswered, condition);                                                                                      // Generate Nico's response (currently just pandorbots)
                        nicoMoveSpeak(nicoResponse.Item1, nicoResponse.Item2, verbalManagerFile, useraudio, condition, userID, time, numturns);
                    }
                    else if (transcript == "problem start")
                    {
                        transcript = transcript + " " + problemStep[0].ToString();

                        nicoResponse = dialogueManager(path, problemStep, speakerSpoke, transcript, time, checkIfAnswered, condition);                                                                                      // Generate Nico's response (currently just pandorbots)
                        nicoMoveSpeak(nicoResponse.Item1, nicoResponse.Item2, verbalManagerFile, useraudio, condition, userID, time, numturns);
                    }
                    else
                    {
                        // make sure topic set to the correct problem and step
                        // detect problem and step we're on, set to that problem and step
                        // don't play response

                        checkIfAnswered = true;

                        // now generate response
                        nicoResponse = dialogueManager(path, problemStep, speakerSpoke, transcript, time, checkIfAnswered, condition);                                                                                      // Generate Nico's response (currently just pandorbots)
                        nicoMoveSpeak(nicoResponse.Item1, nicoResponse.Item2, verbalManagerFile, useraudio, condition, userID, time, numturns);
                    }
               }
               else if (page == "HelloNico")
               {
                    nicoResponse = dialogueManager(path, problemStep, speakerSpoke, transcript, time, checkIfAnswered, condition);                                                                                      // Generate Nico's response (currently just pandorbots)
                    nicoMoveSpeak(nicoResponse.Item1, nicoResponse.Item2, verbalManagerFile, useraudio, condition, userID, time, numturns);
                }
               else
                {
                    SQLLog.InsertLog(DateTime.Now, "problem with page detection", "page string not being filled in", "ResponseGeneration.NicoResponse", 1);
                }

            }
            catch (Exception error)
            {
                SQLLog.InsertLog(DateTime.Now, error.Message, error.StackTrace, "ResponseGeneration.NicoResponse", 1);
            }

            return nicoResponse;

        }

        // This function takes in the speakers transcript and generates Nico's response
        // Output is:
        //              String - Transcript - path of the response file (what Nico said)
        //              Int - Movement - movement code (overwritten later by python movement code)
        //              Int - AnswerStep - did Nico answer this step
        private static Tuple<string, int, string> dialogueManager(string path, List<int> problemStep, int speakerSpoke, string transcript, DateTime time, bool checkIfAnswered, string condition)
        {
            // Return variables
            string answerStep = "no answer";
            int nicoMovementCode = 1;

            string pathTranscriptFile = "";
            string pathResponseFile = "";
            string BOT = "nico";

            if (condition == "control")
            {
                BOT = "nico";
            }
            else
            {
                BOT = "nico";
            }

            try
            {
                // Save transcript to a file so pandora python api program can read it in; save response in a file as well
                pathResponseFile = string.Format("{0}-{1:yyyy-MM-dd_hh-mm-ss-tt}", path + "data\\transcripts\\nlubold_nicoresponse", time) + ".txt";                
                pathTranscriptFile = string.Format("{0}-{1:yyyy-MM-dd_hh-mm-ss-tt}", path + "data\\transcripts\\nlubold_transcript", time) + ".txt";
                StreamWriter transcriptFile = new StreamWriter(pathTranscriptFile);
                transcriptFile.Write(transcript);
                transcriptFile.Close();

                string pythonexe = "C:\\Python27\\python.exe";
                string pythonargs = "C:\\Python27\\NaoNRIPrograms\\VerbalManager\\chatPandoraBot.py " + pathTranscriptFile + " " + pathResponseFile + " " + BOT;

                ExternalMethodsCaller.PythonProcess(pythonexe, pythonargs);

                string nicoResponseText = readResponse(pathResponseFile);
                string lastAnswer = SQLNicoState.ReadNicoState_Answer();
                if (checkIfAnswered && (nicoResponseText.Contains("put the answer") ) )
                {
                    answerStep = "answering";
                }
            }
            catch (Exception error)
            {
                // ** WRITE OUT TO DB
                SQLLog.InsertLog(DateTime.Now, error.Message, error.StackTrace, "ResponseGeneration.generateNicoResponse", 1);
            }

            Tuple<string, int, string> result = new Tuple<string, int, string>(pathResponseFile, nicoMovementCode, answerStep);
            return result;
        }

        // Call to Python code which calls NAO API and enables Nico to move/speak
        private static void nicoMoveSpeak(string nicoresponse, int movementCode, string verbalManagerFile, string useraudio, string condition, string userid, DateTime time, int numturns)
        {
            try
            {
                string pythonexe = "C:\\Python27\\python.exe";
                string formatdate = string.Format("{0:yyyy-MM-dd_hh-mm-ss-tt}", time);
                string pythonargs = verbalManagerFile + userid + " " + formatdate + " " + useraudio + " " + nicoresponse + " " + condition + " " + numturns.ToString();
                ExternalMethodsCaller.PythonProcess(pythonexe, pythonargs);
            }
            catch (Exception error)
            {
                SQLLog.InsertLog(DateTime.Now, error.Message, error.StackTrace, "ResponseGeneration.nicoMoveSpeak", 1);
            }
            
        }


        private static string readResponse(string path)
        {
            if (path == "")
            {
                return "empty transcript";
            }
            else
            {
                return File.ReadAllText(path);
            }
        }
    }
}