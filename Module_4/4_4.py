import random

correct_num = random.randint(1, 10)
guess_num = int(input("The number is between 1 and 10.\nEnter your first guess:"))

while guess_num != correct_num:
    if guess_num > correct_num:
        guess_num = int(input("Too high, try again:"))
    elif guess_num < correct_num:
        guess_num = int(input("Too low, try again:"))

print(f"It's {guess_num}. You are correct!")
