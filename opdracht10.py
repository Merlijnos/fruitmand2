from fruitmand import fruitmand
weight = sorted(fruitmand, key=lambda x: x['weight'], reverse=True)
for i in weight:
    print(i['name'],i['weight'])