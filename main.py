# basik lib emulate http client
import requests
# parser cli argument
import argparse
# metalanguage lineup
import yaml
# serialize request
import json
# find in body item
import re
# import tel bot lib
import telegram
# Handler for tel command
from telegram.ext import CommandHandler
# Handler for tel command
from telegram.ext import Updater


def parse_configs(path):
    """Parse configuration YAML configuration file."""
    with open(path) as cfg:
        config = yaml.load(cfg.read())
    return config



class tebot(object):
    """ Class for iteraction with
    tel Communication."""
    def __init__(self, config_path=None):
        config_path = config_path if config_path is not None \
            else './tel.cfg'
        config = parse_configs(config_path)
        self.auth={}
        self.auth['token'] = config['auth']['token']

    def auth(self, token):
        bot = telegram.Bot(token='self.token')



class Attraction:
    """ Class vor inside logik"""
    def broadcast(self, **kwargs):
        """Entry point function."""
        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)

if __name__ == '__main__':
    Attraction().broadcast()