# exception handling = 프로그램 실행시 문법은 맞으나 실행 중 불가인 상황

# 1) 0으로 숫자 나누기

for x in range(10):
	try:	
		print(int(100/x))
	except ZeroDivisionError:		# ZeroDivisionError 가 발생할 경우
		print("0으로 나눈경우")

# 2) 문자열에 숫자 더하기

try:
	print("string"+100)
except TypeError:
		print("둘의 형이 맞지 않습니다.")

# 3) 문자열과 관계없는 인덱스 호출

string1 = "String"
for x in range(7):
	try:
		print(string1[x])
	except IndexError:
		print("인덱스 범위를 넘었습니다.")
	
# 4) 사전에 없는 키 호출

dic = {"1":1,"2":2}

for x in range(3):
	try:
		print(dic[x])
	except KeyError:
		print("일치하는 키가 없습니다.")
	finally:
		print("finally는 무조건 실행합니다.")
