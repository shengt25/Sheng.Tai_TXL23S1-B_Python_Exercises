def remove_odd_int_list(int_list):
    new_int_list = []
    for num in int_list:
        if num % 2 == 0:
            new_int_list.append(num)
    return new_int_list


int_list = [0, -11, -10, 1, 4, 12, 5, 7, 88, 43, 22, 10]

print(f"Original list: {int_list}\n"
      f"Cut-down list: {remove_odd_int_list(int_list)}")
