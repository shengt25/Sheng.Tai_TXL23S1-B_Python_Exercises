USERNAME = "python"
PASSWORD = "rules"
ERROR_COUNT_MAX = 5

error_count = 0

while True:
    if error_count >= 5:
        print(f"Too many failed attempts.")
        print("Access denied.")
        break
    else:
        input_username = input("Enter username: ")
        input_password = input("Enter password: ")
        if input_username != USERNAME or input_password != PASSWORD:
            error_count += 1
            print(f"Wrong username or password ({error_count} of {ERROR_COUNT_MAX} attempts)\n")
        else:
            print("\nWelcome.")
            break
