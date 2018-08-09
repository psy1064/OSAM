class Calculator:
	def mul(x,y):
		return x * y

	@staticmethod  # 인스턴스를 만들지 않아도 사용 가능
	def add(x,y):
		return x + y
	
	result = 0
	
	@classmethod  # 첫 인수로 클래스 객체 전달
	def total(x,y):
		x.result = x.result + y
		return x.result
	
print(Calculator.mul(10,20))

print(Calculator.add(10,20))

print(Calculator.total(10))


