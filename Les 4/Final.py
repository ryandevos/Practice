def standaardprijs(afstandKM):
    if afstandKM > 0:
        if afstandKM > 50:
            return 15 + afstandKM * 0.6
        else:
            return afstandKM * 0.8
    else: return 0

def ritprijs(leeftijd, weekendrift, afstandKM):
    stnd = standaardprijs(afstandKM)
    if weekendrift == True:
        if leeftijd < 12 or leeftijd >= 65:
            return (stnd * 0.65)
        else: return (stnd * 0.60)
    else:
        if leeftijd < 12 or leeftijd >= 65:
            return (stnd * 0.70)
        else:  return stnd






weekend = input("is het weekend (ja/nee)?")
if weekend[0] in "YyJj":
    weekend = 1;
else:weekend = 0;

leeftijd = eval(input("Wat is je leeftijd: "))
aantalKM = eval(input("Voer het aantal kilometer in: "))

print('De prijs van je kaartje is €' + str("%.2f" % ritprijs(leeftijd, weekend, aantalKM)))