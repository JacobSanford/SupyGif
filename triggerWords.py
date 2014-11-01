"""List of GIFs to interject.
"""

triggers = {
    'amaz(e|ing)': {
        'probability': 20,
        'text': 'Uhhh.. ',
        'targets':
            [
                {
                    'weight': 20,
                    'uri': 'http://i.imgur.com/ivjVA.jpg'
                },
                {
                    'weight': 20,
                    'uri': 'http://www.reactiongifs.com/r/jack.gif'
                }
            ]
    },
    'celebrat(e|ion)': {
        'probability': 25,
        'text': 'Celebrate! ',
        'targets':
            [
                {
                    'weight': 20,
                    'uri': 'http://media1.giphy.com/media/YTbZzCkRQCEJa/giphy.gif'
                },
                {
                    'weight': 10,
                    'uri': 'http://i.imgur.com/3t643vZ.gif'
                },
                {
                    'weight': 10,
                    'uri': 'http://i.imgur.com/4laa7B9.gif'
                },
                {
                    'weight': 5,
                    'uri': 'http://i.imgur.com/Z1PCCTC.jpg'
                }
            ]
    },
    '(jian|gomeshi)': {
        'probability': 50,
        'text': '',
        'targets':
            [
                {
                    'weight': 20,
                    'uri': 'http://www.reactiongifs.com/r/jack.gif'
                }
            ]
    },
    'oops': {
        'probability': 20,
        'text': 'Oops! ',
        'targets':
            [
                {
                    'weight': 20,
                    'uri': 'http://i.imgur.com/YaEedqD.gif'
                }
            ]
    },
    'fail': {
        'probability': 20,
        'text': 'Fail ',
        'targets':
            [
                {
                    'weight': 20,
                    'uri': 'http://38.media.tumblr.com/652767204a0d0d65e016dcfe7a6f8ea0/tumblr_n8kzyuZPUA1qdlh1io1_400.gif'
                }
            ]
    },
    'champagne': {
        'probability': 40,
        'text': 'mmmmMMMaaah-haa...the French...champagne ',
        'targets':
            [
                {
                    'weight': 20,
                    'uri': 'https://www.youtube.com/watch?v=VFevH5vP32s'
                }
            ]
    },
    'roommate': {
        'probability': 70,
        'text': 'Leah\'s Roomate ',
        'targets':
            [
                {
                    'weight': 20,
                    'uri': 'http://i.imgur.com/RiZPQ.gif'
                }
            ]
    },
    'twer(k|king)': {
        'probability': 70,
        'text': 'Twerk  ',
        'targets':
            [
                {
                    'weight': 20,
                    'uri': 'http://i.imgur.com/AZ3LdAh.gif'
                }
            ]
    },
    'worf': {
        'probability': 80,
        'text': 'Soon ',
        'targets':
            [
                {
                    'weight': 20,
                    'uri': 'http://i.imgur.com/a3Xp4Gq.jpg'
                }
            ]
    },
    'welcome': {
        'probability': 33,
        'text': 'Welcome to The Internet! ',
        'targets':
            [
                {
                    'weight': 20,
                    'uri': 'http://i.imgur.com/dOd5yIW.jpg'
                },
                {
                    'weight': 20,
                    'uri': 'http://new4.fjcdn.com/comments/3180221+_bfbd0ea585ec60d40888f3899a5ab625.jpg'
                },
                {
                    'weight': 20,
                    'uri': 'https://c2.staticflickr.com/8/7260/8169906287_ae19c2e85f_z.jpg'
                }
            ]
    }
}
