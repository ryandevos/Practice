def kwadraten_som():
    grondgetallen = [ 4, 5, 3, -81 ]
    return (sum(i**2 for i in grondgetallen if i > 0 ))
print(kwadraten_som())