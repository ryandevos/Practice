from pathlib import Path

def create_file():
    my_file = Path("hardlopers.txt")
    if my_file.exists():
        print("hij bestaat al")
        infile = open('hardlopers.txt', 'a')
        infile.write("hallo \n")
        infile.close()
    else:
        outfile = open('hardlopers.txt', 'w')
        outfile.write("")





create_file()