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
# idx = 0 # idx 라는 변수에 0 (0부터 시작하기 위해서)
# while True: # 무한으로 돌아가게 하기 위해 True
#     idx = b.index(3,idx) # 3이라는 값을 몇번부터 찾을 것인가 idx 0 번 부터시작
#     print(f'3의 값은 {idx}번에 있다.')
#     idx +=1  # 찾은 idx로 부터 +1을 해줘야 같은 곳에서 맴돌지 않고 다음 것을 진행
#     #3이라는 숫자를 더이상 찾지 못하는 경우 에러가 나서 프로그램이 자연스럽게 종료

#for 문
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
print(f'a : {a}') # 맨 앞의 3만 삭제

# pop() = append()의 반대 개념
# 맨 마지막 요소를 빼낸다.(리스트에서 사라진다.)
val = a.pop()
print(f'빼낸 값 : {val} / a : {a}')
val = a.pop()
print(f'빼낸 값 : {val} / a : {a}')

# 리스트 확장(더하기와 비슷한 개념)
print(a)
a.extend(b) # a에 b를 확장(더하는)
print(a)

# count(val) 특정한 값이 해당 리스트에 몇개 있는지 확인
print(a)
print(f'a 안에 3이 {a.count(3)} 개 있다.') 
print(f'a 안에 9가 {a.count(9)} 개 있다.') # 없는 값은 0을 반환

# a 안에 있는 모든 3을 지워주세요

#while 문
while True: #while True(무조건 돌린다)
    a.remove(3)
    if a.count(3) == 0:
        break
print(a)

#for 문
# for n in a:
#     if n == 3:
#         a.remove(3)
# print(a)