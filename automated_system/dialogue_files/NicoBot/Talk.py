__author__ = 'Nikki'
from pb_py import main as API
import sys

# Global parameters
HOST = 'aiaas.pandorabots.com'
USER_KEY = "7d387c332ebfa536b90b7820426ed63b"
APP_ID = "1409611535153"


# gets a response from the bot
def response(text, BOT, debugMode):
    if debugMode == 'trace':
        fullresponse = API.debug_bot(USER_KEY, APP_ID, HOST, BOT, text, session_id=True, reset=True, trace=True,
                           recent=True)
        print "Bot Response: ", fullresponse
    else:
        fullresponse = API.talk(USER_KEY, APP_ID, HOST, BOT, text)
        bot_response = fullresponse['response']

        #session_id = fullresponse['sessionid']
        print BOT + " says: \" ", bot_response, " \" "


# enables continuous talk with the bot
def talk(BOT, debugMode):
    print "Converse with " + BOT + "! When you are finished conversing with " + BOT + ", enter 'quit.' "
    question = raw_input("What would you like to say first? ")
    done = False
    while not done:
        if question == "quit":
            done = True
            break
        else:
            response(question, BOT, debugMode)
            question = raw_input("How would you like to respond?  ")



def main():
    if len(sys.argv) < 3:
        print 'usage: ./Talk.py BOT debugMode'
        sys.exit(1)

    BOT = sys.argv[1]
    debugMode = sys.argv[2]
    talk(BOT, debugMode)

    print "\n\n-------Conversation Done-------"


if __name__ == '__main__': main()