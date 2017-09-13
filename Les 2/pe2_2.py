cijferICOR = 7.5
cijferPROG = 9.6
cijferCSN = 8.2

gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3
beloning = (cijferICOR + cijferPROG + cijferCSN) * 30
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ' ) leveren een beloning van € ' + str(beloning) + ' op!'

print(overzicht)