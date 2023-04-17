import random

Num1 = random.randint(1, 100)
Num2 = random.randint(1, 100)
Num3 = random.randint(1, 100)

print(f"1Num은 {Num1}입니다.")
print(f"2Num은 {Num2}입니다.")
print(f"3Num은 {Num3}입니다.")

M_A_X = max(Num1, Num2, Num3)

print(f"최대값은 {M_A_X}입니다.")