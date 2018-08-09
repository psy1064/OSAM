stringa = "abcdefghi"

print(stringa[0])
print(stringa[5])
print(stringa[8])
print(stringa[-1])  # 역 순

print(stringa[0:3])
print(stringa[1:3])
print(stringa[0:8])  # 0~8까지 문자 출력
print(stringa[:-1])

stringa = "abc"
stringb = "defghi"

print(stringa + stringb)  # 문자열 합치기

print(stringa * 5)  # 문자열 반복

stringa = "오늘도화이팅"

print("도" in stringa)
print("!" in stringa)  # 문자열 중 문자가 있는지 확인

print(len(stringa))  # 문자열 길이

stringa = "오늘도 화이팅"
stringb = "오늘도 \
화이팅"  		# 한줄 문자열  \ = 문자열이 이어지고 있다는 뜻
stringc = """오늘도
화이팅"""		# 여러 줄 문자열

print(stringa)
print(stringb)
print(stringc)

string1 = "Stay hungry, Stay foolish"
# 문자열 검색
print(string1.count("Stay"))		# 문자열이 몇 번 반복되는지
print(string1.find("Stay"))		# 단어가 나오는 위치
print(string1.find("Stay",1))		# 단어가 N+1번째 나오는 위치
print(string1.find("no"))		# 단어가 있는지 없으면 -1 반환 
#print(string1.index("no"))		
print(string1.rindex("Stay"))
#print(string1.startwith("hungry"))	# 단어로 시작하는 문자열 인지
#print(string1.endwith("foolish"))	# 단어로 끝ㅌ나는 문자열 인지

# 문자열 편집
string1 = " Stay hungry "
print(string1)
print(string1.strip())				# 좌우 공백 없애기
print(string1.rstrip())				# 오른쪽 공백 없애기
print(string1.lstrip())				# 왼쪽 공백 없애기
print(string1.replace("hungry","foolish"))	# 문자열 대체

# 문자열 분리
print(string1.split())			# 공백으로 분리
print(string1.split("h"))		# 문자로 분리
