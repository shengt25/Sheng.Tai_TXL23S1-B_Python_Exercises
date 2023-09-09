import random


def dice_roll(sides):
    dice_num = random.randint(1, sides)
    return dice_num


sides = int(input("Enter the number of sides on the dice: "))
print("Dice roll numbers: ", end='')
dice_num = 0
while dice_num < sides:
    dice_num = dice_roll(sides)
    print(dice_num, end=' ')
