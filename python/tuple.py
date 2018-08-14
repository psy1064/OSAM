tuple1 = "Stay", "hungry", 0, 2
# tuple1 = ("Stay", "hungry", 0, 2) -> 괄호 생략 가능
print(tuple1)
print(tuple1[0], tuple1[3])
print(tuple1[2:4])

print(tuple1+(5,1,"Stay","foolih"))		# 연결하기

print("hungry" in tuple1)			# 멤버검사

print(len(tuple1))				# 길이정보

tuple2 = ("Stay", "hungry", ("Stay", "foolish"))
print(tuple2[2])
print(tuple2[2][1])				# 튜플중첩

tuple1 = "Stay", "hungry"
print(tuple1)
list1 = list(tuple1)
print(list1)

list1[1] = "foolish"
print(list1)
tuple1 = tuple(list1)
print(tuple1)					# list, tuple 변환 함수

# 튜플을 사용하는 이유
def addmul(a,b):
	return a+b, a*b

x,y = addmul(100,200)
print("x = ", x, "y = ", y)			# 값을 1개 이상 반환하는 경우

argument = 100, 200
print(addmul(*argument))			# 튜플 값을 함수의 인수로 사용할 경우

print("%d %f %s" %(1000, 1.23, "Stay foolish")) # 서식 문자열을 이용할 때
