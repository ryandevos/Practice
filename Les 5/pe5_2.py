def read_file():
    infile = open('Kaartnummers.txt', 'r')
    content = infile.readlines()
    for user in content:
        splitted = user.split(sep=',')
        print(splitted[1].strip('\n'), 'heeft kaartnummer:', splitted[0])
    infile.close()

read_file()