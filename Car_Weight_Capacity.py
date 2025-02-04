# Car weight capacity

soda = "12"
polvilho = "55"
extra_weight = "5"

def car_weight(soda, polvilho, extra_weight):
    try:
        soda = float(input("Packs of soda: "))
        polvilho = float(input("Bags of polvilho: "))
        extra_weight = float(input("Extra items: "))
    except ValueError:
        print("Numbers only")
        car_weight = soda + polvilho + extra_weight
    if car_weight > 1.300:
        print("Car Overload")
    print(f"total weight: {soda} + {polvilho} + {extra_weight}")
