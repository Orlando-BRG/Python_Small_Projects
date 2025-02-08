# Computer price calculator

def get_valid_input(prompt):
    """Function to get valid numeric input"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Error: Please enter only numeric values.")


def computer_price():
    # Get the cost of each component for computer
    cpu = get_valid_input("CPU: Intel Core i7-13700K: ")
    gpu = get_valid_input("GPU: ASUS ROG Strix NVIDIA GeForce RTX 4070 Ti OC Edition: ")
    motherboard = get_valid_input("Motherboard: ASUS ROG Strix Z790-E Gaming WiFi 6E: ")
    ram = get_valid_input("RAM: G.SKILL Trident Z5 RGB Series 32GB (4 x 16GB) DDR5 7200: ")
    storage = get_valid_input("Storage: 2 x Samsung 990 PRO M.2 2280 2TB PCIe Gen 4.0 SSD: ")
    cooler = get_valid_input("Cooling: NZXT Kraken Elite RGB 360mm AIO CPU Liquid Cooler: ")
    case = get_valid_input("Case: NZXT H9 Elite - All Black: ")
    psu = get_valid_input("Power Supply: Corsair RM850x Fully Modular, 80 PLUS Gold: ")
    extra_cooler = get_valid_input("Additional Cooling: NZXT F120 RGB and RGB Duo Fans (7 x 120mm): ")
    hub = get_valid_input("USB Hub: NZXT Internal USB Hub 3: ")

    total_price = (cpu + gpu + motherboard + ram + storage + cooler + case + psu + extra_cooler + hub)
    return total_price


total_cost = computer_price()

# Apply taxes first
taxes = total_cost * 0.06  # Apply 6% tax first
total_with_taxes = total_cost + taxes  # Add taxes to total first

# Apply discount
discount = total_with_taxes * 0.30  # 30% discount on taxed total
final_price1 = total_with_taxes - discount  # Final price after taxes and discount

# Discount first, then taxes
final_price = total_cost - (total_cost * 0.30)  # Final price after discount but before tax

if total_cost:
    print(f"\n💻 Your computer price is: ${total_cost:.2f}")
    print(f"💰 Taxes (6%): +${taxes:.2f}")
    print(f"🔻 Discount (30%): -${discount:.2f}")
    print(f"✅ Final Price (After Taxes & Discount): ${final_price1:.2f}")
    print(f"✅ Final Price (Before Taxes & Discount): ${final_price:.2f}")
