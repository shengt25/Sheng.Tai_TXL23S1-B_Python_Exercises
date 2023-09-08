inches = 0.0

while True:
    inches = float(input("Enter the length in inches, enter a negative value to stop:\n"))
    if inches >= 0:
        centimeters = inches * 2.54
        print(f"The length in centimeters is: {centimeters}\n")
    else:
        print("Negative value, exiting.")
        break
