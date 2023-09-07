length = float(input("Enter the size in centimeters:\n"))

if length < 42:
    print(f"This zander is too short, {42 - length} cm below the size limit.")
else:
    print("This zander is ok, let's keep it.")
