name_set = set()

while True:
    name = input("\nEnter the name: ")
    if name != "":
        if name not in name_set:
            print("New name.")
            name_set.add(name)
        else:
            print("Existing name.")
    else:
        print("Empty string.")
        for a in name_set:
            print(a)
