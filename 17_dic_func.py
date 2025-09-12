dic = {
    'name':'hong,gil-dong',
    'phone':'010-1234-5678',
    'friends':['Alice','John','Smith']
}

# dic.keys() : 특정한 사전의 키들만 가져와 dic_keys라는 객체를 반환한다
print(dic.keys())

for item in dic.keys():
    print(item)

# dic_keys -> list로 변환
keys = list(dic.keys())
print(keys)

# dic.values() : 특정 사전의 값만 가져와 dict_values 라는 객체를 반환
print(dic.values())

# list 로 변경해서 values 라는 변수에 담아보자
values = list(dic.values()) # dic.values()가 values라는 변수에 list라는 함수로 변환되어 나타남
print(values)

# dic.items() : 사전의 키 값을 한쌍으로 가져와 dict_items로 반환
# 각 키와 값은 () 모양으로 보아 tuple이다.
print(dic.items())
# list로 변환해보면 list 안에 각 키와 값이 tuple로 저장되어 있음을 알 수 있다.
items = list(dic.items()) # list 안에 tuple이 들어가 있는 형태
print(items)

