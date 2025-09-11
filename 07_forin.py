# for 문은 반복 횟수가 정해진 상태에 적합하다. #숫자가 정해진

#물 10잔 떠오기
#for [하나씩 가져올 변수] in [범위]:
for cup in range(1,11):
    print(f'물 {cup} 번째 잔 떠왔습니다.') # range(1,10) = 1부터 9 즉, 10보다 작거나 같다

# 만약 커피를 타는데 한잔의 물에 믹스 2개씩을 넣어야한다면?
# 반복안에 반복이 발생된다.
for cup in range(1,11):
    print(f'물 {cup} 번째 잔 떠왔습니다.') # range(1,10) = 1부터 9

    for mix in range(1,3):
        print(f'{mix} 개의 커피믹스를 넣는다.') # 물 1잔에 믹스 2개라는 안으로 들어가는 구조

        for spoon in range(1,4):
            print(f'{spoon} 번 수푼으로 젓는다.') 

 #   for mix in range(1,3):
 #       print(f'물 {cup} 번째 잔에 커피 믹스 {mix} 개째 넣었습니다.')