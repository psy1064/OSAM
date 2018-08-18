# Stack example
# Stack is LIFO(Last in Firt Out) construction

def printstack(_list):
	for x in range(len(_list)):
		print("순서 = ", x+1, "값 = ", _list[len(_list)-x-1])

stack = []

while True:
	data = input("값을 입력하세요 ")
	if(data == 'q'):
		break
	stack.append(data)

for x in range(len(stack)):
	print("순서 = ", x+1, "값 = ", stack[len(stack)-x-1])	 

printstack(stack)			# 메소드
