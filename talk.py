# init update message
from telegram.ext import Updater
# init message handler
from telegram.ext import CommandHandler
import logging
# metalanguage lineup
import yaml




def parse_configs(path):
    """Parse configuration YAML configuration file."""
    with open(path) as cfg:
        config = yaml.load(cfg.read())
    return config

def activate():
    """debug setup"""
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

class tabot(object):
    """ Class for iteraction with
    tel Communication."""
    def __init__(self, config_path=None):
        config_path = config_path if config_path is not None \
            else './tel.cfg'
        config = parse_configs(config_path)
        self.auth={}
        self.auth['token'] = config['auth']['token']
        print(self.auth)

    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


    def attr(self, ):
        dispatcher = updater.dispatcher
        updater = Updater(token=self.auth['token'])
        start_handler = CommandHandler('start', tabot().start)
        self.dispatcher.add_handler(start_handler)
        updater.start_polling()

if __name__ == '__main__':
    tabot().attr()