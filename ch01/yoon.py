# A and (B or C)
#쉼표를 기준으로 끝는다.

year = int(input("연도를 입렬하시오 : "))

if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) :
    print(year, "년은 윤년입니다.")
else :
    print(year, "년은 윤년이 아닙니다.")
#관계연산자보다 논리연산자가 우선순위가 더 낮다.