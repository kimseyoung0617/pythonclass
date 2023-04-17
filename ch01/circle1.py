x = float(input("x좌표 입력 :"))
y = float(input("y좌표 입력 :"))
l = x**2 + y**2
if l <= 25.0 :
    print(f"({x},{y})점은 원 내부에 있습니다.")
else :
    print(f"({x},{y})점은 원 외부에 있습니다.")
