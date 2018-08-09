a = 19  # 19의 10진수
b = 0o23  # 19의 8진수
c = 0x13  # 19의 16진수
d = 0b10011  # 19의 2진수

print(a,b,c,d)

print(type(a))  # type(parameter) 자료형을 보여주는 함수

print(isinstance(a, int))
print(isinstance(b, int))
print(isinstance(c, int))
print(isinstance(d, int))  # isinstance(object, class or type or tuple) 두 자료형이 같은지 확인하는 함수

a = int('19',16)  # int(string,int) 문자열(숫자)를 진수 변환
print(a)

print(bin(25))  # bin(int) 2진수로 변환
print(oct(25))  # oct(int) 8진수로 변환
print(hex(25))  # hex(int) 16진수로 변환

a = 4.5
print("a =",a)

print(type(a))

print(isinstance(a,float))

b = 4e10
print("b = ",b)

c = -0.594e-15
print("c = ",c)

a = 2 + 9j
b = 10 + 2j

print(a + b)
print(a - b)
print(a * b)
print(a / b)  # 복소수 사칙연산


