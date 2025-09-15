import random

number = random.randint(1,31) # 1~31까지의 숫자를 radom으로 number에 대입
print(f' 내 마음속 숫자: {number}') #random으로 어떤 숫자가 정해졌는지 보여줌(출력문)
running = True # running에 True 대입  #True만 있면 계속실행(무한루프) #False 값이 있어야함

# while 은 오른쪽에 있는 조건 결과가 Ture일 경우 반복되는 구문
# running이 초기에 True 이므로 무조건 실행되는 구조
while running: 
    guess = int(input('1~31 중 내가 생각한 숫자는?'))# 입력받은 값을 정수(int) 로 변환하여 guess에 대입
    print(f'입력받은 숫자 : {guess}') #guess에 숫자를 대입할 수 있는 문자열이 실행

    if number > guess: # 만약 guess가 number보다 작다면 (범위지정)
        print('내가 생각한 숫자보다 작습니다.') # 작다는 것을 알려주는 문자열 출력
    elif number < guess:  # 위 if 열에 해당하지 않는 guess 즉, 만약 guess가 number보다 크다면
        print('내가 생각한 숫자보다 큽니다.') # 크다는 것을 알려주는 문자열 출력
    else: # (number == guess) # 위 if 문과 elif 문에 해당되지 않는 나머지
        print('정답입니다.') # 정답이라는 문자열 출력
        running = False #running 변수는 False 값으로 바뀜
        # 목표값(내마음속 숫자 number)이 나왔기 때문에 반복 while 문을 끝냄

# 내가 생각한 정답
#     if guess < number:
#         print(f'더 큰 숫자 입니다.')
#
#     if guess > number:
#         print(f'더 작은 숫자 입니다.')
#
#     if guess ==  number:
#         print('정답입니다!')
#         running = False

