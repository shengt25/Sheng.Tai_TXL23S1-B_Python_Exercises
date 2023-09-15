def check_dup(airport_dict, icao):
    if icao not in airport_dict.keys():
        return 1
    else:
        overwrite = input("ICAO already exist, do you want to overwrite? (y/n): ")
        if overwrite == "y":
            return 1
        elif overwrite == "n":
            print("Skipped.")
        else:
            print("Invalid option, skipped.")


def add_airport(airport_dict, icao, airport_name):
    airport_dict[icao] = airport_name


def fetch_airport(airport_dict, icao):
    if icao not in airport_dict.keys():
        result = "ICAO not found, please check."
    else:
        result = airport_dict[icao]
    return result


if __name__ == "__main__":
    airport_dict_1 = {}

    while True:
        print("\nOptions: 1.New airport. 2.Fetch information of airport. 3.Quit: ", end="")
        option = int(input())

        if option == 1:
            icao = input("Enter the ICAO: ")
            if check_dup(airport_dict_1, icao) == 1:
                airport_name = input("Enter the name of airport: ")
                add_airport(airport_dict_1, icao, airport_name)

        elif option == 2:
            icao = input("Enter the ICAO: ")
            print(fetch_airport(airport_dict_1, icao))

        elif option == 3:
            print("Goodbye")
            break

        else:
            print("Invalid option.")
