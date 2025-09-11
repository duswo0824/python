# seach 검색 -> 특정한 자료 덩어리에서 원하는 값을 찾는 것
a = [3,4,1,2,3,4,'G','F','G']
# 원하는 값의 인덱스 찾기
# 2라는 값은 어느 위치에 있는가?
print(f'2는 어디? :{a.index(2)}') #a에서 2의 index(방)?
print(f'G는 어디? :{a.index('G')}') # G는 2개지만 처음 찾은 값만 알려줌

# 5번 index 부터 'G'를 찾아라 - 즉, 시작위치(5)
print(f'G는 어디? :{a.index('G',5)}')
# 값이 없으면 에러(예외)를 발생 시킨다.
# print(a.index('H')) # ValueError: 'H' is not in list

b = [3,4,1,2,3,4,5,6,1,3,2] # 모든 3을 찾아 보세요.

# 기본
# idx = b.index(3) # 0
# print(f'3의 값은 {idx}번에 있다.')
# idx = b.index(3,1) # 4
# print(f'3의 값은 {idx}번에 있다.')
# idx = b.index(3,5) # 9
# print(f'3의 값은 {idx}번에 있다.')
# idx = b.index(3,10)  # ValueError: 3 is not in list
# print(f'3의 값은 {idx}번에 있다.')

# while 문
idx = 0
#while True:
#    idx = b.index(3,idx)
#   print(f'3의 값은 {idx}번에 있다.')
#   idx += 1

for n in b:
     if n == 3:
        print(f'3이 있는 인덱스{idx}')
     idx += 1

# 내가 한 방법
# print(b.index(3)) # 0
# print(b.index(3,1)) # 4
# print(b.index(3,5)) # 9
# print(b.index(3,10)) # ValueError: 3 is not in list

# 리스트 list 요소 삭제
# del a[3]과 a. remove(3)
# del 은 특정 인덱스의 값을 지운다. # 3번 인덱스의 값 삭제
# remove 는 해당 값을 지운다.(한개만) # 3을 삭제 (하나만)

print(f'a : {a}')
a.remove(3)
print(f'a : {a}')