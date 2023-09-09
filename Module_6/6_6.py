import math


def pizza_unit_price(diameter, price):
    area = (diameter / 100) ** 2 * math.pi
    unit_price = price / area
    return unit_price


unit_price = []
for i in range(1, 3):
    print(f"\n- Pizza #{i}:")
    diameter = float(input("Enter the diameter in centimeters: "))
    price = float(input("Enter the price in euros: "))
    unit_price.append(pizza_unit_price(diameter, price))

if unit_price[0] < unit_price[1]:
    print("\nPizza #1 has better value of money.")
elif unit_price[0] > unit_price[1]:
    print("\nPizza #2 has better value of money.")
else:
    print("\nThey have the same value of money.")

print(f"{unit_price[0]:.2f} euros/m2 vs {unit_price[1]:.2f} euros/m2.")