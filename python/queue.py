# Queue example
# Queue is FIFO(first in first out) construction

def printqueue(_list):
	for x in range(len(_list)):
		print("순서 = ", x+1, "데이터 = ", _list[x])
queue = []

while(1):
	i = input('값을 입력하세요')
	if(i=='q'):
		break
	queue.append(i)

for x in range(len(queue)):
	print("순서 = ", x+1, "데이터 = ", queue[x])

printqueue(queue)
