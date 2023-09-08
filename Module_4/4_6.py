import random

count_inside_circle = 0

total_number = int(input("Enter the total number:"))

i = 1
while i <= total_number:
    i += 1
    coord_x = random.uniform(-1, 1)
    coord_y = random.uniform(-1, 1)
    if coord_x ** 2 + coord_y ** 2 < 1:
        count_inside_circle += 1

pi = 4 * count_inside_circle / total_number
print(f"Approximation of pi: {pi}")
