scores = 95
if(scores >= 90):
    print("축하드립니다.")  # 90점 이상이면 축하드립니다. 출력
else:
    print("다음에 더 잘하실 수 있습니다.")  # 아니면 이 문구 출력

scores = input('scores=')  # scores 출력 후 입력 받기 -> 문자열로 저장
print(scores)

scores = int(input('scores='))  # scores 출력 후 입력 받기 -> 문자열을 정수로 형변환
print(scores)

print("scores = " + str(scores))  # 문자열 + 문자열 출력 위해 scores 문자열로 형변환

number = int(input('Input Numbers = '))

if(number > 0):
    print("양수입니다.")
elif(number < 0):
    print("음수입니다.")
else:
    print("0입니다.")  # 숫자 입력 받고 양수, 음수 판별

stock = int(input('input stocks'))
if(stock <= 5):
    print("재고가 곧 부족해 집니다. 추가 주문하세요.")
elif(stock >= 6 and stock <= 10):  # and 연산자
    print("재고가 충분합니다.")
elif(stock >= 11):
    print("다른 곳으로 물품 " + str(stock-10) + "개를 이동해야 합니다.")  # 형 변환
