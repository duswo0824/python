# 팀별 함수list
# 반환타입 : O  매개변수 : O # 음료 자판기 -  버튼in 음료 out

def machine(drink):
    print(f'{drink}가 나왔습니다.')
    return f'시원한{drink}'

hand = machine('포카리')
print(hand)

# 반환타입 : O  매개변수 : X # 정수기 - in 물 out

def water():
    return '물이 나오는 중' #반환되는 것 : 물

cup = water()
print(cup)

# 반환타입 : X  매개변수 : O # 쓰레기 통 (쓰레기 in, - out)

def garbage(trash):
    print(f'{trash} 버림')
    
garbage('종이컵')

# 반환타입 : X  매개변수 : X # 스탠드 - in - `out

def lamp():
    print('불이 켜짐')

lamp()

# 헷갈리는 내용 정리

# 반환타입 : O  매개변수 : O
def 토스트기(bread): # 선언 : 만들어만놨지 누가 사용한 건 아님
    print(f'{bread}이 구워지고 있다.') # 실질적 동작이 아님, 사람 눈에만 보이는 것
    return f'구워진{bread}' # 실제 밖으로 나오는 값

# 사용 : 선언한 것을 실행
토스트기('베이글') # 그냥 이것만 하면 갈 곳이 없어짐 # 베이글이 구워지고 있다.

dish = 토스트기('베이글') #return으로 나온 값을 dish에 담는다.
print(dish) #dish 안의 값을 출력

print(토스트기('크림빵')) #토스트기에서 나온 값을 바로 출력

# 반환타입 : O  매개변수 : X

def 번호표기계():
    return "번호표" #실제로 무언가 나오는 것

print(번호표기계())

# 반환타입 : X  매개변수 : O
def 저금통(coin):
    print(f'{coin}원 저축')

저금통(500)
# 저금통에는 return이 없는데 저금통이 실행후 나온곳에 출력
# print(저금통(100)) None이 출력되는 것

# 반환타입 : X  매개변수 : X
def 호출벨():
    print('진동이 울림') # 받는것이 없다. 즉, 내가 확인하는것

호출벨() #밖으로 내뱉는게 없으니 print쓰지 않음