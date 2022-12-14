from fruitmand import fruitmand
for names in fruitmand:
    if names['name']=='druif':
        fruitmand.remove(names)
colors=[]
for color in fruitmand:
    if color['color'] in colors:
        pass
    else:
        colors.append(color['color'])
        print(color['color'])