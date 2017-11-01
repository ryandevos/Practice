def read_file():
    infile = open('Kaartnummers.txt', 'r')
    content = infile.readlines()
    lenght = len(content)
    numb_lijst = []
    for user in content:
        item = user.split(sep=',')
        numbers = item[0]
        numb_lijst.append(numbers)
    numb_lijst.sort()
    infile.close()


    print("Deze file telt ", lenght, "regels")
    print("Het grootste  kaartnummer is: ", numb_lijst[-1], "en dat staat op regel " )

read_file()