from fruitmand import fruitmand
opnieuw = True
colors = []
listcolors = []
colors=[]

for x in range(len(fruitmand)):
    listcolors.append(fruitmand[x]['color'])
while opnieuw == True:
    for color in fruitmand:
        if color['color'] in colors:
            pass
        else:
            colors.append(color['color'])
    color = input('Kies een kleur: '+ str(colors)).lower()
    if color not in listcolors:
        continue
    for x in range(len(fruitmand)):
        if fruitmand[x]['color'] == color:
            colors.append(fruitmand[x]['round'])
    rond = colors.count(True)
    nrond= colors.count(False)
    som = (rond-nrond)
    if som <0:
        som = abs(som)
        print('Er zijn',som, 'meer niet ronde dan ronde vruchten van de kleur',color)
        break
    elif som >0:
        print('Er zijn',som, 'meer ronde vruchten dan niet ronde')
        break
    elif som == 0:
        print('Er zijn evenveel ronde als niet ronde vruchten')
        break