talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

pounds = pounds + talents * 20
lots = lots + pounds * 32
grams = lots * 13.3

kilograms = int(grams / 1000)
grams = grams - kilograms * 1000
print(f"\nThe weight in modern units:\n{kilograms} kilograms and {grams:.2f} grams.")
