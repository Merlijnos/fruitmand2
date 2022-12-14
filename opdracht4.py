from fruitmand import fruitmand
import random
aantal = int(input('Noem een aantal '))
fruit=random.choice(fruitmand)
for i in range(aantal):
    print(fruit['name'])

