pr = int(input("물건값을 입력하시오: "))
note = int(input("1000원 지폐개수: "))
co500 = int(input("500원 동전개수: "))
co100 = int(input("100원 동전개수: "))

ch = note*1000 + co500*500 + co100*100 - pr

n500 = ch // 500
n100 = (ch % 500) // 100
print("500원 = ", n500, "100원 =", n100)