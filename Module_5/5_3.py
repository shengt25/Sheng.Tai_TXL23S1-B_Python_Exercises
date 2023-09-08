num = int(input("Enter a integer: "))
prime_flag = True

if num < 1:
    print("Invalid number, it needs to be greater than 0. (0 excluded).")
elif num == 1:
    print("1 is not a prime number.")
else:
    for i in range(2, num - 1):
        if num % i == 0:
            prime_flag = False
            break

    if prime_flag:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
