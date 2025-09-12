# dictionary (사전)은 {키 : 값} 형태로 되어있다.
# 비슷한 자료구조로는 자바스크립트에 오브젝트, 자바에 맵이 있다.
dic = {
    'name':'Lee yeon jae',
    'phone':'010-1234-5678',
    'age':25
}

dic2 ={
    'name':'Ally',
    'phone':'010-8765-4321',
    'friends':['Alice','John','Smith']
}

# 사전에 데이터 넣기 1
a = {'first':'a'}
print(a)
# 사전에 데이터 넣기 2
a['second'] = 'b'
print(a)
# 사전에서 특정 요소 삭제
del a['second']
print(a)