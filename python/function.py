def firstfunc(a):  # 함수 생성 def func_name(parameter)
	print(a)

def add(a, b):
	return(a+b)  # 두 매개변수를 더하는 함수
	
a = input('input number = ')
firstfunc(a)

print(add(3,4))
print(add(3.14,6.28))
print(add("abc","bcd"))  # 매개변수 형식에 구애 X


