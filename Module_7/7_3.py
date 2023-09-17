def add_airport(airport_dict, icao):
    if icao not in airport_dict.keys():
        airport_name = input("Enter the name of airport: ")
        airport_dict[icao] = airport_name
    else:
        overwrite = input("ICAO already exist, do you want to overwrite? (y/n): ")
        if overwrite == "y":
            airport_name = input("Enter the name of airport: ")
            airport_dict[icao] = airport_name
        elif overwrite == "n":
            print("Skipped.")
        else:
            print("Invalid option, skipped.")


def fetch_airport(airport_dict, icao):
    if icao not in airport_dict.keys():
        result = "ICAO not found, please check."
    else:
        result = airport_dict[icao]
    return result


if __name__ == "__main__":
    airport_dict_1 = {}

    while True:
        option = input("\nOptions: 1.Add new airport. 2.Fetch information of airport. 3.Quit: ")

        if option == "1":
            icao = input("Enter the ICAO: ")
            add_airport(airport_dict_1, icao)

        elif option == "2":
            icao = input("Enter the ICAO: ")
            print(fetch_airport(airport_dict_1, icao))

        elif option == "3":
            print("Goodbye")
            break

        else:
            print("Invalid option.")
