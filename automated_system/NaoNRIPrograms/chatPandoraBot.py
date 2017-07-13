from pb_py import main as API
import sys

# Global parameters
HOST = 'aiaas.pandorabots.com'
USER_KEY = "7d387c332ebfa536b90b7820426ed63b"
APP_ID = "1409611535153"
BOT = "nico"

   
def response(transcriptFile, pathForResponse):
    fileWrite = open(pathForResponse, 'w')
    with open(transcriptFile) as f:
        for line in f:
            response = API.talk(USER_KEY, APP_ID, HOST, BOT, line)
            bot_response = response['response']
            fileWrite.write(bot_response)
    fileWrite.close()

def main():
    fileOfTranscript = sys.argv[1]
    pathForResponse = sys.argv[2]
        
    response(fileOfTranscript, pathForResponse)

if __name__ == '__main__': main()