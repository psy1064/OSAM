class C1:  # C1 클래스 생성
	a = 1
	b = 2  # C1 클래스 멤버변수

print("C1\'s a = ", C1.a, "C1\'s b = ", C1.b)

x = C1()  # 인스턴스 생성 C++로 표현하면 C1 x;
x.a = 10
print("x\'s a = ", x.a)

y = C1()
y.a = 999
print("y\'s a = ", y.a)

class Soju:
	water = 0
	alchol = 0
	ingredient = 0
	volume = 0

truedew = Soju()

truedew.water = 78
truedew.alchol = 21
truedew.ingredient = 1
truedew.volume = 360

print("물 = ",truedew.water,"%")
print("알콜 = ",truedew.alchol,"%")
print("기업비밀 = ",truedew.ingredient,"%")
print("용량 = ",truedew.volume,"ml")

# print(dir(C1))  C1 클래스 속성 출력
# del C1.b  b 변수삭제
