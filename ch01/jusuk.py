fir = int(input("첫번째 정수 : "))
sec = int(input("두번째 정수 : "))

if fir < sec :
    max = sec
elif fir > sec:
    max = fir
else:
    max = "없습니다."
print(f"큰수는 {max}")