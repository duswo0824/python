# 파스칼표기법 - 맨 앞글자만 대문자(Java의 class 생성시 활용)
# 카멜표기법 - 단어의 의미가 있는 첫글자를 대문자(shopList)
#스네이크 표기법 ** python - 단어간의 구분을 _(shop_list)

# 리스트 생성 방법 1 - 비어있는 리스트로 생성
a = []

# 리스트 생성 방법 2 - 값이 있는 리스트로 생성 * 흔하진 않음
shop_list = ['apple','mango','carrot','banana']
print(f'shop_list:{shop_list}')

# 리스트에 값을 넣는 방법
# 가장 뒤로부터 넣는 방법
a.append(1) # append : 추가 # 0번방
a.append(2) # 1번방
a.append(3)
# 특정한 번호를 지정해서 넣는 방법
a.insert(1,'X')  # insert : 해당 인덱스 값을 뒤로 미루고 그자리
# 1번방에 2를 밀어내고 X를 넣음

print(f'a 의 길이 : {len(a)}') # a의 전체 길이(len)?
print(f'a:{a}')  #[1,X,2,3] 일때 0번방에 1 인것 즉, 0,1,2,3번방

# a의 2번방에 있는 값
print(f'a[2]={a[2]}')
# a의 가장 마지막 방에 있는 값 : a의 길이(len) -1
print(f'a의 마지막 방의 값={a[3]}')
# 길이에서 1을 뺀 값을 이용 -> 인덱스는 0번부터 시작한다는 점을 이용
print(f'a의 마지막 방의 값={a[len(a)-1]}')
# python에서만 사용되는 방식, 0보다 뒤로 가면 맨 뒤로 이동된다는 개념(-1)
print(f'a의 마지막 방의 값={a[-1]}')

# 리스트 정렬(sort) - 말 그대로 정렬하는 것
shop_list.sort() # 오름차순 (작은수가 위로 큰수가 아래로)
print(f'shop_list:{shop_list}')

shop_list.sort(reverse=True) # 내림차순 (큰수가 위로 작은수가 아래로)
print(f'shop_list:{shop_list}')

# sorted 는 원본의 리스트를 정렬한 값을 새로운 리스트로 반환 (원본 회손X)
new_list = sorted(shop_list)
print(f'new_list:{new_list}')

# a의 2번 인덱스(방)에 c를 넣는다.
# insert는 해당 인덱스 값을 뒤로 미루고 그자리에 들어간다.
# insert와 다른점은 해당 인덱스의 값을 지우고 그자리에 들어간다.
a[2] = 'c'
print(f'a:{a}')

# list 삭제
del a[1] # 1번 인덱스를 삭제
print(f'a:{a}')

