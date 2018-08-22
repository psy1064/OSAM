# 파일 만들기
text = """testing
writing text
in the files
"""

files = open('fileIO.txt','w')		# 쓰기 전용
print(files)

files.write(text)			# file에 내용 넣기
files.close()

# 한글 저장하기
with open('fileIO1.txt','w', encoding = 'utf-8') as files:
	files.write("한글 만세!!")
# with ~ as
# with open('data.txt','r') as f: = f = open('data,txt','r')
	
# 줄단위로 쓰기
lines = ['line #1\n', 'line #2\n', 'line #3\n']
files = open('fileIO2.txt','w')		
files.writelines(lines)			# 문자열 리스트를 파일에 씀

# 줄단위로 읽기
files = open('fileIO2.txt')
print(files.read())			# 파일을 읽어옴
					# readline() 줄 하나를 읽어들인다.
					# readlines() 전체 줄을 리스트에 넣어서 반환

files.close()				# 파일을 닫는다.
