import random

dice_sum = 0
dice_count = int(input("How many dice do you like to roll: "))
for i in range(dice_count):
    dice_num = random.randint(1, 6)
    dice_sum += dice_num

print("The sum of numbers is:", dice_sum)
