cup = 0
running = True

# while running:
#     cup += 1  # += 더해서 대입 (cup + 1)
#     print(cup)
#     if cup == 10:
#         # running = False
#         break  # cup이 10이 되면 종료
#
# print('while 문 종료')

for i in range(1,10):

    # if i ==3:
    #     continue

#3,6,9를 제외한 숫자만 실행

    # or 조건
    if i ==3 | i ==6 | i==9:
        continue

    # 나머지
    if i % 3 == 0:
        continue

    # 멤버 연산자
    if i in [3,6,9]: #i 안에 3,6,9가 포함되어 있다면?
        continue

    print(i)