# init update message
from telegram.ext import Updater
# init message handler
from telegram.ext import CommandHandler
import logging
# for parse config
import yaml


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
updater = Updater(token='366401853:AAE8IEvYxANZiywH7_IQMnzMfhr11jERJPw')
dispatcher = updater.dispatcher

def parse_configs(path):
    """Parse configuration YAML configuration file."""
    with open(path) as cfg:
        config = yaml.load(cfg.read())
    return config

config_path = './tel.cfg'
config = parse_configs(config_path)
token = config['auth']['token']
print(token)



def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def attr():
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()

if __name__ == '__main__':
    attr()