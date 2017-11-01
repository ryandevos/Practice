def table():
    print('{:^9}''{:^5}'.format('F', 'C'))
    for i in range(-30, 41, 10):
        print('{0:5}''{1:8.1f}'.format(i * 1.8 + 32, i))



table()