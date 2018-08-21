# class inheritance example 
# 1)
class Queue(list):
	enqueue = list.append
	def dequeue(self):
		return self.pop()

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)

print(queue)

print(queue.dequeue())
print(queue.dequeue())

print(queue)

# 2)

class Calculator:
	def __init__(self):		# 생성자
		self.result = 0
		print("Calculaotr class init")

	def add(self,num1,num2):
		self.result = num1 + num2
		return self.result
	def sub(self,num1,num2):
		self.result = num1 - num2
		return self.result

class UpgradeCal(Calculator):		# Calculator class 상속
	def __init__(self):
		self.result = 0
		print("UpgradeCal inherited Calculator clsss init")
	def mul(self, num1, num2):
		self.result = num1 * num2
		return self.result
	def div(self, num1, num2):
		self.result = num1 / num2
		return self.result


test = Calculator()
print(test.add(2,3))
print(test.sub(3,4))

test1 = UpgradeCal()
print(test1.add(3,4))
print(test1.mul(3,4))
