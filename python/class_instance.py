class soju:
	water = 0
	alchol = 0
	ingrediandt = 0
	volume = 0 		# 클래스 멤버

truedew = soju()
truedew.water = 78
truedew.alchol = 21
truedew.ingrediant = 1
truedew.volume = 360		# 인스턴스 멤버

# 클래스 내부에서 멤버를 생성하고 사용하는 방법
# 1) Unbound Method Call : 첫 인수가 해당 클래스의 인스턴스 객체

class GeneralMethod:
	def set(self, v):
		self.value = v
	def get(self):
		return self.value

classInstance = GeneralMethod()
print(GeneralMethod.set)

GeneralMethod.set(classInstance, 'Unbound Method Call')
print(GeneralMethod.get(classInstance))

# 2) Bound Method Call : 첫 인수로 인스턴스 객체가 자동 전달

classInstance2 = GeneralMethod()
print(classInstance2)

print(classInstance2.set)
classInstance2.set("Bound Method call")
print(classInstance2.get())
