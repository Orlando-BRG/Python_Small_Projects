# Car weight capacity

soda = 12
polvilho = 55
extra_weight = 5

def car_weight(soda, polvilho, extra_weight):
    try:
        soda = int(input("Packs of soda: "))
        polvilho = int(input("Bags of polvilho: "))
        extra_weight = int(input("Extra items: "))
    except ValueError:
        print("Numbers only")
        car_weight = soda + polvilho + extra_weight
    if car_weight > 1.3:
        print("Car Overload")
    print(f"total weight: {soda} + {polvilho} + {extra_weight}")
