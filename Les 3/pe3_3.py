leeftijd = eval(input("Geef je leeftijd:"))
pas = input("Nederlands paspoort (ja/nee):")


if leeftijd >= 18 and pas == "ja":
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("Helaas, je mag nog niet stemmen!")