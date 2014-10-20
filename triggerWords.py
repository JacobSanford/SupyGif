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
                    'weight': 5,
                    'uri': 'http://i.imgur.com/Z1PCCTC.jpg'
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
    }
}
