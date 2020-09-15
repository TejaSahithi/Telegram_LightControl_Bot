pip install adafruit_io
import os
ADAFRUIT_IO_USERNAME = os.getenv("ADAFRUIT_IO_USERNAME") # get it from adafruit.io
ADAFRUIT_IO_KEY = os.getenv("ADAFRUIT_IO_KEY")
from Adafruit_IO import Client,Feed
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
new = Feed(name='telegrambot')
result = aio.create_feed(new)
result
from Adafruit_IO import Data
pip install python-telegram-bot
from Adafruit_IO import Client,Data
from telegram.ext import Updater,CommandHandler
def on(telegrambot,update):
  chat_id = update.message.chat_id
  aio.create_data('telegrambot',Data(value = 1))
  telegrambot.send_message(chat_id =chat_id,text ="lights on")

def off(telegrambot,update):
  chat_id = update.message.chat_id
  aio.create_data('telegrambot',Data(value = 0))
  telegrambot.send_message(chat_id =chat_id,text ="lights off")

u = Updater('958085870:AAHycGlc4K_GJ24zOtKiSh9z6NX26uQeOc4')   # Use Telegram Token HTTP API
dp =u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle() 
