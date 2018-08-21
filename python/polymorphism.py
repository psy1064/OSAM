class Animal:
	def cry(self):
		print("./././")
	def supertest(self):
		print("상속받은 클래스입니다.")

class Human(Animal):
	def cry(self):
		print("엉엉")
		super().supertest()			# super() = 상속받은 클래스에서 부모클래스의 함수를 사용하고 싶을때

class Whale(Animal):
	def cry(self):
		print("고래")

class Monkey(Animal):
	def cry(self):
		print("우끼끼")

for i in (Human(), Whale(), Monkey()):
	i.cry()
