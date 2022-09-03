# coding: utf-8
from telethon import TelegramClient, events
from time import sleep
import os, re
from subprocess import getoutput



#id number and api hash for log in the account 
api_hash = ''
api_id = ''

#Instance of client
client = TelegramClient('{}/test'.format(os.environ['HOME']), api_id, api_hash)


@client.on(events.NewMessage(chats='PresidenteAMLO'))
async def messageH(event):
    testing = event.raw_text
    if re.search('(?i).?conferencia.*prensa.*matutina.?', testing):
        testing = re.search('https://you.*', testing)
        if testing:
            testing = testing.group(0)
            testing = testing.split()
            testing = testing[0]
            minutes = 0
            while minutes < 180:
                sleep(60)
                minutes += 1
            os.system('youtube-dl -Uicvxf bestaudio -R 50 -o \%\(title\)s\.\%\(ext\)s --write-thumbnail --audio-format mp3 --embed-thumbnail --add-metadata --write-description {}'.format(testing))
            testing = getoutput('youtube-dl -se {}'.format(testing))
            await client.send_file('lamaaudio', '{}/{}.mp3'.format(os.environ['HOME'], testing))

client.start()
client.run_until_disconnected()
