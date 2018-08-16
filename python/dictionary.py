volume = {"truedew":360,"goodday":360,"hanrasan":375}	# 사전 선언

keys = ["truedew", "goodday", "hanrasan"]
values = [360,360,375]
temp = zip(keys, values)				# 데이터를 순서대로 묶어줌
volume5 = dict(temp)					# 사전 선언 함수

print(volume5)
print(volume)

print(volume.keys())					# 키에 해당하는 사전 뷰를 반환
print(volume.values())					# 값에 해당하는 사전 뷰를 반환
print(volume.items())					# 항목(key, value)에 해당하는 사전 뷰를 반환

print(volume.clear())					# 모든 요소를 삭제 또는 { }
volume = {"truedew":360,"goodday":360,"hanrasan":375}	
print(volume.get("goodday"))				# get(key값) key값에 해당하는 value 반환
print("hanrasan" in volume)				# 해당 키가 있는지 딕셔너리 안에서 조사

