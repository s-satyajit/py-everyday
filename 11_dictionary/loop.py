car = {
    "brand": "Ford",
    "model": "mustang",
    "year" : 1968
}

for x in car:
    print(car[x])

for x in car.values():
    print(x)

for x, y in car.items():
    print(x, y)