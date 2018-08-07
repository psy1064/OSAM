result = 0
result = 1+2+3+4+5+6+7+8+9+10
print(result)  

result = 0 
i = 0 
while(i<10):
	i += 1
	print(i, end = ' ')  # end = ' ' 출력 시 공백 추가
	result += i
print(result)  # while 이용한 1~10 더하기

x = 0
result = 0
for x in range(0,10):  #  x >= 0 and x < 10
	x += 1
	print (x, end = ' ')
	result += x
print(result)  # for - range 이용한 1~10 더하기

base = 2
i = 1
while(i < 10):
	print(base, " x ", i, " = ", base*i)
	i += 1
print(end = '\n')  # while문 이용한 구구단(2단) 출력

i = 1
for i in range(1,10):
	print(base, " x ", i, " = ", base*i)
	i += 1 
print(end = '\n')  # for문 이용한 구구단(2단) 출력
