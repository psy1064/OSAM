class Student:
	old=-1
	def __init__(self, name, old=17):	# 생성자
		self.name = name		
		self.old = old
	def print_name(self):			# 함수를 명시할때 self를 포함해줘야함 호출 시는 X
		print(self.name)		# c++의 this->name=name 과 같은 맥락
	def print_old(self):
		print(self.old)

s = Student("철수",16)

Student.print_name(s)				# 클래스를 통한 함수 호출, 객체를 parameter로 전달
						# unbound method call
s.print_name()					# 인스턴스 객체에 bind 된 함수 호출
						# bound method call

print("철수의 나이 : ", s.old)
del(s.old)
print("철수의 나의 : ", s.old)

print("철수의 이름 : ", s.name)
del(s.name)
print("철수의 이름 : ", s.name)			# 에러 발생
