# 문자열은 '' 나 '"" 모두 사용가능
name = 'Lee yeon jae' # 문자열  '' (싱글쿼터) 사용 통일
content = "My Content"

# 여러줄의 문자열을 변수에 담을때
multi = '''this is multi line string
this is second line'''

print('name:'+name)
print('content:'+content)
print('multi:'+multi)

# 문지열에 다른 타입의 데이터를 함께 출력할 경우
age = 25

print('내이름은 {0}이고, 나이는 {1} 입니다.'.format(name,age))
print('내이름은 '+name+'이고, 나이는 '+str(age)+'입니다.') #str()이라는 함수 사용하면 문자열
print(f'내이름은 {name}이고, 나이는 {age} 입니다.') #f-string 은 문자열 +@ 같이 가능

# 여러줄 -> 한줄 처리, 한중 -> 여러줄처럼 줄바꿈
print('이것은 한줄이지만 \n여러줄처럼 보이게 할겁니다.') #\n (new line) : 줄바꿈
print('이것은 두줄이지만 \
한줄처럼 보이게 할겁니다.') # \ (역슬래시) : 아래와 같은 줄로 인식
                                # enter, 들여쓰기 할 경우 다른걸로 인식 


