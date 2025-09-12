# set 은 순서가 없고, 중복을 허용하지 않는다.
number_set = set([1, 2, 3])
print(number_set) #dic 과 비슷하게 생겼으나 키X 값만 존재

# 중복을 제외하고 담는다.
# 그래서 중복 제거 용도로 사용된다
str_set = set('HelloWorld')
print(str_set) #{'l', 'W', 'H', 'r', 'o', 'e', 'd'} 순서 무작위 & 중복제거

# set : 집합의 의미를 가짐
# set 들을 이용해서 집합을 구현할 수 있다.
s1 =set([1,2,3,4,5,6])
s2 =set([4,5,6,7,8,9])

# 교집합(intersection) # and(&) # a와 b에 있는거 가져오기
print(f'교집합 : {s1&s2}')
print(f'교집합 : {s1.intersection(s2)}') # 함수 intersection (s1에 s2를 교집합)

# 합집합(union) # or(|) # a또는 b에 있는거 가져오기(set 중복제거)
print(f'합집합 : {s1|s2}')
print(f'합집합 : {s1.union(s2)}')

# 차집합(minus|difference)
print(f'차집합 : {s1-s2}') # 앞의 기준에서 빼낸다 앞에 것만 남는다
print(f'차집합 : {s1.difference(s2)}')
print(f'차집합 : {s2-s1}')
print(f'차집합 : {s2.difference(s1)}')

# 값 1개 추가하기
# 여러개 추가하기
# 특정값 제거