__author__ = 'Nikki'
from pb_py import main as API
import sys

# Global parameters
HOST = 'aiaas.pandorabots.com'
USER_KEY = "7d387c332ebfa536b90b7820426ed63b"
APP_ID = "1409611535153"


# gets a response from the bot
def response(text, BOT):
    fullresponse = API.talk(USER_KEY, APP_ID, HOST, BOT, text)
    bot_response = fullresponse['response']
    #session_id = fullresponse['sessionid']
    print BOT + " says: \" ", bot_response, " \" "


# enables continuous talk with the bot
def talk(BOT):
    print "Converse with " + BOT + "! When you are finished conversing with " + BOT + ", enter 'quit.' "
    question = raw_input("What would you like to say first? ")
    done = False
    while not done:
        if question == "quit":
            done = True
            break
        else:
            response(question, BOT)
            question = raw_input("How would you like to respond?  ")


def main():
    if len(sys.argv) < 2:
        print 'usage: ./Talk.py BOT'
        sys.exit(1)

    BOT = sys.argv[1]
    talk(BOT)

    print "\n\n-------Conversation Done-------"


if __name__ == '__main__': main()