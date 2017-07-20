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
        public static Tuple<string, int, string> NicoResponse(string path, List<int> problemStep, int speakerSpoke, string transcript, DateTime time)
        {

            Tuple<string, int, string> nicoResponse = new Tuple<string, int, string>("",1,"no answer");
            bool checkIfAnswered = false;

            try
            {
                // Get whether the current step has been answered and pass that along 
                int currentstep = problemStep[1];
                int answerKey = problemStep[3];
                string answerPattern = SQLAnswerPattern.GetAnswerPattern(answerKey)[1];
                char[] chAnswerPattern = answerPattern.ToCharArray();

                if (transcript == "" || transcript == null)                                                                                                          // Need to handle when there is no transcript - will depend on if this is the first time we've been here or not
                {
                    //transcript = problemStep[0].ToString() + "_" + problemStep[1].ToString();
                    transcript = "no response";
                    nicoResponse = dialogueManager(path, problemStep, speakerSpoke, transcript, time, checkIfAnswered);                                                                                      // Generate Nico's response (currently just pandorbots)
                    nicoMoveSpeak1(nicoResponse.Item1, nicoResponse.Item2);
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
                    nicoResponse = dialogueManager(path, problemStep, speakerSpoke, transcript, time, checkIfAnswered);                                                                                      // Generate Nico's response (currently just pandorbots)
                    nicoMoveSpeak1(nicoResponse.Item1, nicoResponse.Item2);
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

                    nicoResponse = dialogueManager(path, problemStep, speakerSpoke, transcript, time, checkIfAnswered);                                                                                      // Generate Nico's response (currently just pandorbots)
                    nicoMoveSpeak1(nicoResponse.Item1, nicoResponse.Item2);
                }
                else if (transcript == "problem start")
                {
                    transcript = transcript + " " + problemStep[0].ToString();

                    nicoResponse = dialogueManager(path, problemStep, speakerSpoke, transcript, time, checkIfAnswered);                                                                                      // Generate Nico's response (currently just pandorbots)
                    nicoMoveSpeak2(nicoResponse.Item1, nicoResponse.Item2);
                }
                else 
                {
                    // make sure topic set to the correct problem and step
                    // detect problem and step we're on, set to that problem and step
                    // don't play response
                    string tempTrans = problemStep[0].ToString() + " " + problemStep[1].ToString();
                    string pythonexe = "C:\\Python27\\python.exe";
                    string pythonargs = "C:\\Python27\\NaoNRIPrograms\\chatPandoraBot_topicSet.py " + tempTrans;
                    ExternalMethodsCaller.PythonProcess(pythonexe, pythonargs);

                    checkIfAnswered = true;

                    nicoResponse = dialogueManager(path, problemStep, speakerSpoke, transcript, time, checkIfAnswered);                                                                                      // Generate Nico's response (currently just pandorbots)
                    nicoMoveSpeak1(nicoResponse.Item1, nicoResponse.Item2);
                }
                //nicoResponse = dialogueManager(path, problemStep, speakerSpoke, transcript, time, checkIfAnswered);                                                                                      // Generate Nico's response (currently just pandorbots)
                //nicoMoveSpeak(nicoResponse.Item1, nicoResponse.Item2);                                                                                                  // Call python to speak

            }
            catch (Exception error)
            {
                SQLLog.InsertLog(DateTime.Now, error.Message, error.StackTrace, "ResponseGeneration.NicoResponse", 1);
            }

            return nicoResponse;

        }

        private static Tuple<string, int, string> dialogueManager(string path, List<int> problemStep, int speakerSpoke, string transcript, DateTime time, bool checkIfAnswered)
        {
            // Return variables
            string answerStep = "no answer";
            int nicoMovementCode = 1;

            string pathTranscriptFile = "";
            string pathResponseFile = "";


            try
            {
                // Save transcript to a file so pandora python api program can read it in; save response in a file as well
                pathResponseFile = string.Format("{0}-{1:yyyy-MM-dd_hh-mm-ss-tt}", path + "data\\transcripts\\nlubold_nicoresponse", time) + ".txt";                
                pathTranscriptFile = string.Format("{0}-{1:yyyy-MM-dd_hh-mm-ss-tt}", path + "data\\transcripts\\nlubold_transcript", time) + ".txt";
                StreamWriter transcriptFile = new StreamWriter(pathTranscriptFile);
                transcriptFile.Write(transcript);
                transcriptFile.Close();

                string pythonexe = "C:\\Python27\\python.exe";
                string pythonargs = "C:\\Python27\\NaoNRIPrograms\\chatPandoraBot.py " + pathTranscriptFile + " " + pathResponseFile;

                ExternalMethodsCaller.PythonProcess(pythonexe, pythonargs);

                string nicoResponseText = readResponse(pathResponseFile);
                string lastAnswer = SQLNicoState.ReadNicoState_Answer();
                if (checkIfAnswered && (nicoResponseText.Contains("put the answer") ) )
                {
                    //|| nicoResponseText.Contains("Answer") || lastAnswer == "confirming answer"))

                    //if (lastAnswer == "confirming answer")
                    //{
                    //    answerStep = "answering";
                    //}
                    //else
                    //{
                    //    answerStep = "confirming answer";
                    //}

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
        private static void nicoMoveSpeak1(string path, int movementCode)
        {
            try
            {
                string pythonexe = "C:\\Python27\\python.exe";
                string pythonargs = "C:\\Python27\\NaoNRIPrograms\\simpleGestureSelectionForAutomatedSys.py " + path;
                ExternalMethodsCaller.PythonProcess(pythonexe, pythonargs);
            }
            catch (Exception error)
            {
                SQLLog.InsertLog(DateTime.Now, error.Message, error.StackTrace, "ResponseGeneration.nicoMoveSpeak", 1);
            }
            
        }

        private static void nicoMoveSpeak2(string path, int movementCode)
        {
            try
            {
                string pythonexe = "C:\\Python27\\python.exe";
                string pythonargs = "C:\\Python27\\NaoNRIPrograms\\nico_move_speak.py " + path;
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