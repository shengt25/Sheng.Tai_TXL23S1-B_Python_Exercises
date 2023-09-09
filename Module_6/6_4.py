def sum_int_list(int_list):
    sum_int = 0
    for num in int_list:
        sum_int += num
    return sum_int


int_list = [1, 52, 42, 5, 61, 14, 1, 24]

print(sum_int_list(int_list))
