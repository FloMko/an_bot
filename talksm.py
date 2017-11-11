# init update message
from telegram.ext import Updater
# init message handler
from telegram.ext import CommandHandler
# echo handler
from telegram.ext import MessageHandler, Filters
import logging
# for parse config
import yaml
# parse response
import json


def parse_configs(path):
    """Parse configuration YAML configuration file."""
    with open(path) as cfg:
        config = yaml.load(cfg.read())
    return config

config_path = './tel.cfg'
config = parse_configs(config_path)
token = config['auth']['token']


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
updater = Updater(token=token)
dispatcher = updater.dispatcher




def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def info(bot, update):
    r = str((bot.get_me()))
    # print(r)
    bot.send_message(chat_id=update.message.chat_id, text=r)


def attr():
    start_handler = CommandHandler('start', start)
    info_handler = CommandHandler('info', info)
    echo_handler = MessageHandler(Filters.text, echo)
    updater.start_polling()
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(info_handler)

if __name__ == '__main__':
    attr()