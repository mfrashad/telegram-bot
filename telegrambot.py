import sys
import time
import telepot

#LED
def on():
    print('on')
    return

def off():
    print('off')
    return

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == 'on':
       bot.sendMessage(chat_id, on())
    elif command =='off':
       bot.sendMessage(chat_id, off())

bot = telepot.Bot('693823025:AAGZ0NMB9oi-63WZCyasq07y3Gj3HYTmvSA')
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        exit()

    except:
        print('Other error or exception occured!')
