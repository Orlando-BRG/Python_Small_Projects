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

# Car weight capacity calculator

# Weight of each item (in lbs)
soda_weight = 12  # Each pack of soda weighs 12 lbs
polvilho_weight = 55  # Each bag of polvilho weighs 55 lbs
extra_item_weight = 5  # Each extra item weighs 5 lbs

def car_weight():
    try:
        # User input: Number of packs and bags
        soda_count = int(input("Packs of soda: "))
        polvilho_count = int(input("Bags of polvilho: "))
        extra_count = int(input("Extra items: "))

        # Calculate total weight
        total_weight = (soda_count * soda_weight) + (polvilho_count * polvilho_weight) + (extra_count * extra_item_weight)

        # Check if weight exceeds limit
        if total_weight > 1300:
            print("Car Overload! 🚨 The weight exceeds the 1,300 lbs limit!")
        else:
            print(f"Total weight: {total_weight:.2f} lbs ✅")

    except ValueError:
        print("❌ Error: Please enter only numbers.")

# Run the function
car_weight()
