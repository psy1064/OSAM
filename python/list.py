list1 = ["Stay","hungry",0,2]

print(list1[0], list1[3])
print(list1[2:4])  			# print(list1[2],list1[3])
print(list1+[5,1,"Stay","foolish"])  	# 연결하기
print(list1*2)  			# 반복하기
print("hungry" in list1)  		# 멤버검사
print(len(list1))			# 길이정보

list1[2] = list1[2] + 20 		# 값 변경
print(list1)
list1[2:4] = [777,888]			# 치환
print(list1)
list1[4:4] = ["Stay", "foolish"]	# 추가
print(list1)
list1[4:6] = []				# 삭제
print(list1)
del list1[0]				
print(list1)

list2 = ["Stay", "foolish", ["Stay", "foolish"]]

print(list2[2])
print(list2[2][1])

list1 = ["Stay", "foolish", 0, 2]

list1.append(7)				# 마지막 인덱스에 추가
print(list1)
list1.insert(3,7)			# 3번째 자리 인덱스에 추가
print(list1)
print(list1.index("foolish"))		# 인덱스 자리를 위치 
print(list1.count(7))			# 값을 몇개 가지고 있는지 

list2 = [2,6,1,4,5,0]
list2.sort()				# 정렬
print(list2)
list2.reverse()				# 역순
print(list2)

list1.remove(0)				# 값을 삭제
print(list1)
list1.pop(1)				# 인덱스 위치에 있는 값을 삭제
print(list1)

