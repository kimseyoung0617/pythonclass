hours = int(input("근무시간을 입력하시오 : "))
wage = int(input("시간당 임금을 입력하시오 : "))
if hours <= 40 :
	totalWages = wage * hours
else :
    overtime = hours - 40
    totalWages = wage * 40 + (1.5 * wage) * overtime

print(f"총임금은 {totalWages:.5f}원 입니다.")