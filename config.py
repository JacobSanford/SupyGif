import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('SupyGif', True)

SupyGif = conf.registerPlugin('SupyGif')
conf.registerChannelValue(SupyGif,'enable',registry.Boolean('False',"""Enable displaying messages from SupyGif in channel?"""))
