#arr모듈 c언어의 배열과 같다
#어떤 변수든 저장이 가능하다.
#수정가능 변수를 묶어놓은것과 비슷하다.
#객체. 속성 a = n[:] 복사가능
#자료형이 같아야 비교가능 예외 : 숫자의 경우 실수와 정수는 비교가능 복소수는 안됨.
#a>4 or a<-4 , a<4 and a >1 and와 or로 쓴다. 3<a<5도 파이썬은 가능. 다른언어는 어의 안됨.
#list는 0부터 비교 커지는 수로 비교한다.
n = int(input("Enter a number"))
flag = n % 2
#산술연산이 비교연산보다 우선순위가 높다.
print(bool(flag == 0))

score = int(input("점수를 입력하세요 : "))
if score >= 60 :
    print("합격입니다.")
else :
    print("불합격입니다.")
    
a = 50
print(f'a = {a}')
if a < 100 :
    print("1000 보다 작군요.")
prit("프로그램 종료")

a = int(input("정수를 입력하세요 : "))
print(f"a = {a}")
if a < 100:
    print("100보다 작군요.")
else :
    print("100과 같거나 크군요.")
print("프로그램 끝")

geam = float(input("짐의 무게는 얼마입니까?(kg)"))

if geam < 20.0 :
    print("짐에 대한 수수료는 없습니다.")
else :
    print("무거운 짐은 20000만원을 내셔야합니다.") 
print("감사합니다.")

"""주석"""
