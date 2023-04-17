print("숫자게임에 오신 것을 환영합니다.")
number=283
answer=int(input("숫자를 입력하시오: "))
while answer!=number:
    if answer>283:
        print("크다")
    elif answer<283:
        print("작다")
    answer=int(input("다시해: "))    

print("맞았습니다")        

 