import random
def game(rows, cols):
    'a simple bomb finding game'

    # generate a list of size rows*cols that contains
    # empty strings except for 1 'B' at some random index
    table = (rows*cols-1)*[''] + ['B']
    random.shuffle(table)

    while True:
        pos = input('Enter next position (format: x y): ')
        position = pos.split()
        # position (x, y) corresponds to index x*cols + y of table
        if table[int(position[0])*cols + int(position[1])] == 'B':
            print('You found the bomb!')
            break
        else:
            print('No bomb at position', pos)
game()