import pandas as pd

def syncLogs(userFile, nicoFile, errorFile, audioFile):
    user = pd.read_csv(userFile, names=["StateKey","UserID","DateTime","SessionID","ProblemID","StepID","DialogueAct","DialogueActConfidence","Spoke","StepAnswer","ClickStep","NumAuto","transcript"],infer_datetime_format=True)
    nico = pd.read_csv(nicoFile, names=["NicoState","UserID","DateTime","SessionID","ProblemID","StepID","NicoMovement","AnswerKey","Answered","NicoResponse","FilePath"])
    #error = pd.read_csv(errorFile)
    #audio = pd.read_csv(audioFile)

    # Get the length of each, which ever one is longer, create an empty dataframe of that length with # of columns equal
    # to user columns + nico columns + audio columns + error columns

    userSize = user.shape
    nicoSize = nico.shape

    alldata = pd.DataFrame(index=range(0, (userSize[0] + nicoSize[0])), columns = ["UserID","DateTime","SessionID","ProblemID","StepID","Owner","DialogueAct","DialogueActConfidence","Spoke","StepAnswer","ClickStep","NicoMovement","Answered","Transcript"])


    # loop through user
    # if row time equals row time in nico, then insert both
    # if nico is > then, then just insert user
    # if nico is < then, then just insert nico
    # if error == insert error
    # if audio == insert audio
    # with insertion, first column is DateTime, second column UserID, third is SessionID, ProblemID, StepID [1-5]
    # then user values: DialogueAct, DialogueActConfidence, Spoke, StepAnswerKey, ClickStep, transcript [6 - 11]
    # then nico values: NicoMovement, AnswerKey, AnsweredStep, NicoResponse [6 - 9]
    # audio values: AudioKey, UserID, DateTime, FilePathAudio, ProblemID, StepID, SessionID, Prosody_Pitch
    # error values: LogKey, DateTime, UserID, ProblemID, StepID, SessionID, ErrorCode, ErrorMessage, FormName, StackTrace

    alldataIndex = 0;
    index = 0;
    if userSize[0] > nicoSize[0]:
        for i, row in user.iterrows():
            #print row['UserID'], row['DateTime'], row['SessionID'], row['ProblemID'], row['StepID']
            userDateTime = row['DateTime']
            userDate = userDateTime.split(" ")[0]
            userTime = userDateTime.split(" ")[1]

            nicoDateTime = nico.iloc[index]['DateTime']
            nicoDate = nicoDateTime.split(" ")[0]
            nicoTime = nicoDateTime.split(" ")[1]

            if userDate == nicoDate:
                if userTime == nicoTime:
                    alldata.loc[alldataIndex:alldataIndex,0:5] = user.iloc[1, 1:5]
                    alldata.loc[alldataIndex]["Owner"] = "user"
                    alldata.loc[alldataIndex:alldataIndex,7:11] = user.iloc[index, 6:10]
                    alldata.loc[alldataIndex]["Transcript"] = user.iloc[index]["transcript"]

                    alldataIndex += 1

                    alldata.iloc[alldataIndex:alldataIndex, 0:5] = nico.iloc[index, 1:5]
                    alldata.loc[alldataIndex]["Owner"] = "nico"
                    alldata.iloc[alldataIndex, 12] = nico.iloc[index, 6]
                    alldata.iloc[alldataIndex, 13] = nico.iloc[index, 8]
                    alldata.iloc[alldataIndex]["Transcript"] = nico.loc[index]["NicoResponse"]

                    alldataIndex =+ 1
                    index += 1

            for i,r in alldata.iterrows():
                print r








def main():
    '''
    if len(sys.argv) != 5:
        print 'usage: ./readfile2.py socialCodes transcriptfileDirectory outputFileNumTurns outputFileWhichTurns'
        sys.exit(1)
    '''

    userFile = "C:\\Nikki\\ASU_Research\\NRI_Project\\System\\NRI_Git_Hub\\automated_system\\LogSync\\data\\userresults.csv"
    nicoFile = "C:\\Nikki\\ASU_Research\\NRI_Project\\System\\NRI_Git_Hub\\automated_system\\LogSync\\data\\nicoresults.csv"
    errorFile = ""
    audioFile = ""
    syncLogs(userFile, nicoFile, errorFile, audioFile)


if __name__ == '__main__': main()