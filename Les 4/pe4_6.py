def wijzig(letterlijst):
    letterlijst[:] = []
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')


letter = ['a', 'b', 'c']

print(letter)
wijzig(letter)
print(letter)