import random


def dice_roll():
    dice_num = random.randint(1, 6)
    return dice_num


print("Dice roll numbers: ", end='')
dice_num = 0
while dice_num < 6:
    dice_num = dice_roll()
    print(dice_num, end=' ')
