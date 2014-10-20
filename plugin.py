"""Supybot plugin for injecting GIF image links based on trigger phrases
"""

import operator
import random
import re
import time
import supybot.callbacks as callbacks
import supybot.ircmsgs as ircmsgs
from supybot.commands import *
import triggerWords

__author__ = "Jacob Sanford"
__copyright__ = "Copyright 2014"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Jacob Sanford"
__email__ = "jsanford@unb.ca"
__status__ = "Production"

class SupyGif(callbacks.Plugin) :
    threaded = True
    def doPrivmsg(self, irc, msg) :
        if(self.registryValue('enable', msg.args[0])):
            matches_to_display = []
            for match_phrase, match_data in triggerWords.triggers.iteritems():
                match = re.search(
                                  match_phrase,
                                  msg.args[1],
                                  re.IGNORECASE
                                  )
                if match:
                    if random.randint(0, 100) < match_data['probability']:
                        gif_image = GifImage(match_phrase, ).get()
                        if gif_image:
                            matches_to_display.append(
                                {
                                    'uri': gif_image['uri'],
                                    'weight': gif_image['weight'],
                                    'text': match_data['text']
                                }
                            )

            if len(matches_to_display) > 0:
                sorted_images = sorted(matches_to_display, key=lambda k: k['weight'])
                time.sleep(random.random() * 5)
                irc.queueMsg(
                             getattr(ircmsgs,'privmsg')(
                                             msg.args[0],
                                             sorted_images[0]['text'] + sorted_images[0]['uri']
                                             )
                             )

class GifImage(object):
    def __init__(self, phrase):
        self.possibleimages = []
        self.phrase = phrase
        self.total_weight = 0
        self.load()
    def add(self, target):
        self.total_weight += target['weight']
        self.possibleimages.append(target)
    def get(self):
        if self.total_weight is 0:
            return False
        winning_number = random.randint(0, self.total_weight)
        running_total = 0
        for cur_target in self.possibleimages:
            running_total += cur_target['weight']
            if running_total >= winning_number:
                return {'uri': cur_target['uri'], 'weight': cur_target['weight']}
    def load(self):
        for phrase, phrase_data in triggerWords.triggers.iteritems():
            if phrase is self.phrase:
                for cur_target in phrase_data['targets']:
                    self.add(cur_target)

Class = SupyGif
