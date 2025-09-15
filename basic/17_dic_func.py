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

# 값을 가져오기
print(dic.get('name')) # get 메서드 활용
print(dic['phone'])

# dic 안에 있는 모든 키와 값을 키:값 형태로 출력해 보자
# 1. 키를 뽑아낸 다음, 키를 가지고 값을 뽑아내는 방법
for keys in dic.keys():
    print(f'{keys}: {dic[keys]}')  # 값을 가져오는 방법 dic[keys]
# 2. 키와 값을 동시에 뽑아낸 다음 거기서 키와 값을 각각 추출하는 방식
for items in dic.items():
    # print(items) # ('name', 'hong,gil-dong')으로 출력 tuple형태 
    print(f'{items[0]}: {items[1]}') #즉, tuple이 불러오는 방식 : print(tu1[1]) 사용
    
#내가 한 방법
# keys = list(dic.keys())
# print(f'{keys[0]}:{dic['name']}, {keys[1]}:{dic["phone"]}, {keys[2]}:{dic["friends"]}')

members = {
    'kim':63, 'lee':88, 'park':97, "gang":77, "hwang":100, "ga":65,
    "na":92, "la":90, "wang":100, "gu":79
}
# 90이상인 사람의 이름만 출력
for item in members.items(): # members의 키와 값을 둘다 가져온다 # kim:63 (0번방 : 1번방)
    if item[1]>=90: # 1번방이 점수
        print(f'이름 : {item[0]}') #이름만 출력하는 것이기 때문에 0번방만
        #print(f'이름 : {item[0]} 점수 : {item[1]}') # 둘다 뽑아낸다면?

# 내가 한 방법
# 만약 members에 있는 사람의 점수가 90 점 이상이라면? 이름만 출력
# for keys in members.keys():
#     if members[keys] >= 90:
#         print(keys)

# key in dic : 해당 키가 사전에 존재하는지 확인 
# 검색 시작 여부를 결정할 수 있는 방법
yn = 'kim' in members
print(f'kim 이 있는가? {yn}')

yn = 'jung' in members
print(f'jung 이 있는가? {yn}')

# update : 이미 있는 키면 수정을, 없는 키면 추가를 하는 함수
dic.update({'name':'홍길동','age':30,'married':False})
print(dic) #이름은 있는키 한글 홍길동으로 수정 나머지는 없는 키

# dic.clear() : 사전안의 내용을 모두 지운다.
dic.clear()
print(dic)  # {} 로 출력
