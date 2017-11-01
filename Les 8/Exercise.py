import random

def game():
    bomx = random.randrange(0, 5)
    bomy = random.randrange(0, 5)
    bomfound = 0

    while bomfound == 0:

        pos = input('Enter next position (format: x y): ')

        positionsplit = pos.split()
        positionnum = []
        positionnum.append(int(positionsplit[0]))
        positionnum.append(int(positionsplit[1]))

        if positionnum[0] == bomx and positionnum[1] == bomy:
            print("Gefeliciteerd je hebt de bom gevonden!")
            bomfound = 1
        else:
            print("Helaas de bom ligt hier niet")
            print("de bom lag op:", bomx, " ", bomy)

game()