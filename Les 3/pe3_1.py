import time
score = eval(input('Geef je score: '))
goed = "Gefeliciteerd!"
fout = "Helaas!"
geslaagd = "Met een score van " + str(score) + " ben je geslaagd!"
gezakt = "Met een score van " + str(score) + " ben je gezakt!"

if score > 15:
    print(goed)
    time.sleep(1)
    print(geslaagd)
else:
    print(fout)
    print(gezakt)
