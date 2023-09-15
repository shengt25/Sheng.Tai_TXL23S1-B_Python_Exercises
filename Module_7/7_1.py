seasons = ("spring", "summer", "autumn", "winter")

month = int(input("Enter the month number: "))
if month == 12 or 1 <= month <= 2:
    print(seasons[3])
elif 3 <= month <= 5:
    print(seasons[0])
elif 6 <= month <= 8:
    print(seasons[1])
elif 9 <= month <= 11:
    print(seasons[2])
else:
    print("Invalid month")
