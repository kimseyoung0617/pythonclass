print("숫자게임에 오신 것을 환영합니다.")
number=int(input("숫자를 맞춰: "))
answer=350
while number!=answer:
    if number<answer: #if문은 들려쓰면 안에다 넣기
        print("작다")
    elif number>answer: #elif를 써
        print("크다")    
    number=int(input("다시해: ")) 
    
print("맞았어")