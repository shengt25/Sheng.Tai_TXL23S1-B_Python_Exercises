import random

code1_int = [random.randint(0, 9) for i in range(3)]
code1_str = ''.join(list(map(lambda a: str(a), code1_int)))

code2_int = [random.randint(1, 6) for i in range(4)]
code2_str = ''.join(list(map(lambda a: str(a), code2_int)))

print(f"Combination lock #1: {code1_str}")
print(f"Combination lock #2: {code2_str}")
