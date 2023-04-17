string = input("문자열을 입력하시오 : ")
length = len(string)
if lengh % 2 == 1 :
    ch1 = stromg[lengrh // 2]
	print("중앙글자는 ", ch1)
else :
    ch1 = string[length // 2 - 1]
	ch2 = string[lenth // 2]
	print("중앙글자는 ", ch1, ch2)