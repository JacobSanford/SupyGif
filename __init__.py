"""Supybot plugin for injecting GIF image links based on trigger phrases.
"""

import supybot
import supybot.world as world

__version__ = "main"
__author__ = supybot.Author("Jacob Sanford", "JS", "jsanford@unb.ca")
__contributors__ = {}
__url__ = 'https://github.com/JacobSanford/SupyGif'

import config
import plugin
reload(plugin)

if world.testing:
    import test

Class = plugin.Class
configure = config.configure
