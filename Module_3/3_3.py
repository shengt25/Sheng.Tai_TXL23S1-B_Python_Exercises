gender = input("Enter your biological gender (male / female): ")

if gender != "male" and gender != "female":
    print("Invalid biological gender.")
else:
    hemoglobin = float(input("Enter your hemoglobin value (g/l): "))
    hemoglobin_level = ""

    if gender == "female":
        if hemoglobin < 117:
            hemoglobin_level = "low"
        elif 117 <= hemoglobin <= 155:
            hemoglobin_level = "normal"
        else:
            hemoglobin_level = "high"
        print(f"\nYour hemoglobin value is {hemoglobin_level}.")
    else:
        if hemoglobin < 134:
            hemoglobin_level = "low"
        elif 134 <= hemoglobin <= 167:
            hemoglobin_level = "normal"
        else:
            hemoglobin_level = "high"
        print(f"\nYour hemoglobin value is {hemoglobin_level}.")