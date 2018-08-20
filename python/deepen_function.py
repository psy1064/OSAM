def add(a,b):
	return a + b

addfunc = add				# 함수 저장
print(addfunc(100,200))

def f(g,a,b):				# 함수를 인수로 전달 
	return g(a,b)

print(f(add,200,300))

def deco(type='italic'):
	def italic(s):
		return '<i>' + s + '</i>'
	def bold(s):
		return '<b>' + s + '</b>'
	if type=='italic':
		return italic		# 함수 반환
	else:
		return bold		# 함수 반환

dec = deco()
print(dec('안녕하세요 반갑습니다.'))

l = lambda : 1
print(l())

def add(x,y):
	return x+y

print("function = ",add(10,20))

add = lambda x,y : x+y			# 람다 함수 : 이름이 없는 한줄짜리 함수  
					# lambda <인수> : <반환할 식>
print("lambda = ",add(10,20))
