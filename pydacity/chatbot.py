import sys
import irc.bot
import requests

from threading import Thread
from utilities import *
from pipe import *
from main import *

lastRunTime = 0
CommandList = []
DTMFList = []


class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        fitInWindow()
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        # Get the channel id, we will need this for v5 API calls
        url = 'https://api.twitch.tv/kraken/users?login=' + channel
        headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r['users'][0]['_id']
        
        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print('Connecting to ' + server + ' on port ' + str(port) + '...')
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:'+token)], username, username)
        

    def on_welcome(self, c, e):
        print('Joining ' + self.channel)
        lastRunTime = time.time()
        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        username = getUsername(e.tags)
        if(validateUsername(username)):
            inputList = e.arguments
            joinedList = ''.join(inputList)
            encodedList = cleanEncoding(joinedList)
            first = joinedList[0]
            if(first == "!"):
                encodedList = encodedList[1:]
                CommandList.append(encodedList)
            else:
                DTMFList.append(encodedList)

class Batcher(Thread):   

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for e in CommandList:
            parseCommand(e)
        DTMF(DTMFList)
        DTMFList.clear()
        CommandList.clear()
        autoplay()
        time.sleep(16)
        self.run()

def main():
    username  = 'Replace this'
    client_id = 'Replace this'
    token     = 'Replace this'
    channel   = 'Replace this'

    t = Batcher()
    t.setName("t")
    t.start()
    bot = TwitchBot(username, client_id, token, channel)
    bot.start()

if __name__ == "__main__":
    main()