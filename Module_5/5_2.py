num_list = []

print("Enter the numbers, enter empty to end:")
while True:
    str_input = input()
    if str_input == "":
        break
    else:
        num_list.append(float(str_input))

num_list.sort(reverse=True)

print("The five greatest numbers:")
for i, num in enumerate(num_list):
    if i < 5:
        print(num)
