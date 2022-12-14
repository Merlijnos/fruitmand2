from fruitmand import fruitmand
fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 1700,
    'color' : 'green',
    'round' : True
})

totaal = 0
for fruit in fruitmand:
    gewicht = fruit['weight']
    totaal += gewicht
print(totaal)