"""List of GIFs to interject.
"""

triggers = {
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
    }
}
