num_list = []

print("Enter the numbers, enter empty value to end inputting:")

# 1. Enter numbers
while True:
    str1 = input()
    if str1 == '':
        break
    else:
        num_list.append(float(str1))

# 2. Compare
num_list_len = len(num_list)
if num_list_len == 0:
    print("No number entered, exiting.")
else:
    value_min = num_list[0]
    value_max = num_list[0]
    i = 0
    while i < num_list_len:
        if value_min < num_list[i]:
            value_min = num_list[i]
        if value_max > num_list[i]:
            value_max = num_list[i]
        i += 1
    print(f"The largest value is {value_max}, the smallest value is {value_min}")
