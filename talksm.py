# init update message
from telegram.ext import Updater
# init message handler
from telegram.ext import CommandHandler
# echo handler
from telegram.ext import MessageHandler, Filters
# download photo 
from telegram import File, Bot
#"""This module contains an object that represents a Telegram File."""
from os.path import basename
from os.path import abspath


import logging
# for parse config
import yaml
# parse response
import json

from scii import *


def parse_configs(cfg_path):
    """Parse configuration YAML configuration file."""
    with open(cfg_path) as cfg:
        config = yaml.load(cfg.read())
    return config

config_path = './tel.cfg'
config = parse_configs(config_path)
token = config['auth']['token']


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
updater = Updater(token=token)
dispatcher = updater.dispatcher


def get_image(bot, update):
    # bot.send_message(chat_id=update.message.chat_id, text=update.message.photo)
    p =(update.message.photo)
    chat_id=update.message.chat_id
    print(chat_id)
    file_id=(p[-1]['file_id'])
    file_path=abspath('./pic/'+file_id)
    bot.get_file(file_id).download(custom_path=file_path)
    main(file_id)
    file_name = ('./pic/'+file_id+'lum')
    file_open = open(file_name, 'rb')
    bot.sendDocument(chat_id=chat_id, document=file_open)

#def send_image(bot, update):
#    bot.send_photo(chat_id=update.message.chat_id, photo =file_path+'lum')
    


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def info(bot, update):
    r = str((bot.get_me()))
    # print(r)
    bot.send_message(chat_id=update.message.chat_id, text=r)

def close():                                                                                
    updater.stop()

def attr():
    start_handler = CommandHandler('start', start)
    info_handler = CommandHandler('info', info)
    echo_handler = MessageHandler(Filters.text, echo)
    photo_handler = MessageHandler(Filters.photo, get_image)

    updater.start_polling()
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(info_handler)
    dispatcher.add_handler(photo_handler)

if __name__ == '__main__':
    attr()
