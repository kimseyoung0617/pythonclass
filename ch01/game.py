print("숫자게임에 오신 것을 환영합니다.")
number=62

q=input("1부터 100 사이의 숫자를 추측해보세요.")

guess=int(q)

if guess==number:
    print("맞았습니다.")
	
else:
    print("틀렸습니다.")
    print("게임이 종료됩니다.")