tu1 = (1,2,3) # tuple은 []가 아닌 ()로 선언 # 수정과 삭제 안됨
tu2 = ('a','b','c')
tu3 = (1,2,('a','b'))

# 불러오기
print(tu1[1])
# slicing
print(tu2[1:]) #1번 부터 보여주고.. 끝까지
# 더하기
print(tu1+tu2)
# 곱하기(반복)
print(tu1*3)

# tuple <-- --> list 간의 전환
tu2list = list(tu2)
print(f'{tu2}->{tu2list}') # ()에서 []로 변환 #list가 되어 수정 삭제 가능

list2tu = tuple(tu2list)
print(f'{tu2list}->{list2tu}')
