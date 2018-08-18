# 알고 싶은 단을 입력하면 해당하는 단을 보여주는 프로그램

i = input('단을 입력하세요')
print(i, "단을 알고싶으신가요?")
for x in range(1,10):
	print(i, "x", x, "=", int(i)*x)		# i는 문자열이므로 int형 변환
	x += 1
