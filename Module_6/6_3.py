def gallons_to_liters(gallons):
    return gallons * 3.785


while True:
    gallons = float(input("Enter the quantity of gallons: "))
    if gallons < 0:
        print("Negative value, exiting.")
        break
    else:
        print(f"{gallons} gallons equal to {gallons_to_liters(gallons)} litres.\n")
