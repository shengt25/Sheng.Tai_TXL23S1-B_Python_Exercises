talents = float(input("Enter talents:\n"))
pounds = float(input("\nEnter pounds:\n"))
lots = float(input("\nEnter lots:\n"))

pounds = pounds + talents * 20
lots = lots + pounds * 32
grams = lots * 13.3

kilograms = int(grams / 1000)
grams = grams - kilograms * 1000
print(f"The weight in modern units:\n{kilograms} kilograms and {grams:.2f} grams.")
