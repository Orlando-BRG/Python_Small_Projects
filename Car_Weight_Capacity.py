# Car weight capacity calculator

# Weight of each item (in lbs)

soda_weight = 12  # Each pack of soda weights 12 lbs
polvilho_weight = 55  # Each pack of polvilho weights 55 lbs
extra_item_weight = 5  # Each extra item weights 5 lbs


def car_weight():
    try:
        # User input: number of packs and bags
        soda_count = int(input("Packs of soda: "))
        polvilho_count = int(input("Bags of polvilho: "))
        extra_item_count = int(input("Extra items: "))

        # Calculate total weight
        car_weight = (soda * polvilho * extra_weight)
    if car_weight > 1.3:
        print("Car Overload")
    print(f"total weight: {soda} + {polvilho} + {extra_weight}")

except ValueError:
        print("Numbers only")

#Project in progress in between machines