from ai import *

color_map = {
    '0': '',
    '1': 'RED',
    '2': 'ORANGE',
    '3': 'YELLOW',
    '4': 'LIME_GREEN',
    '5': 'LIGHT_GREEN',
    '6': 'DARK_GREEN',
    '7': 'LIGHT_BLUE',
    '8': 'DARK_BLUE',
    '9': 'PURPLE',
    'a': 'GRAY',
    'b': 'PINK',
    'c': 'BROWN',
}

state = [
    '3283',
    '53ba',
    '8b84',
    'a136',
    '5a91',
    '28c4',
    '6719',
    '47bc',
    '5b6c',
    'c976',
    'a245',
    '7291',
    '0000',
    '0000'
]

if __name__ == '__main__':

    s = [[color_map[c] for c in row] for row in state]
    bot = AI(s, max_depth=50)
    win, moves = bot.solve([])
    if win:
        print('Bot won! Moves: ', moves)
    else:
        print('Bot lost :( Are you sure you put in the right state?')
