# 주석 = 컴퓨터는 알 수 없고,  사람만 알 수 있는 언어
# 이름 = 값
int = 123 # 정수
float = 3.14 # 실수
octal = 0o117 # 8진수(숫자0과 알파벳o를 추가한게 특징)
hex = 0x8ff # 16진수(숫자0과 알파벳x를 추가한게 특징)

# print('int: '+int) # 문자+숫자 형태로는 출력해주지 않는다.
# f-string을 사용하면 문자열과 다른 타입의 데이터를 함께 출력할 수 있다. #문자열끼리는 사용X
print(f'int: {int}') # print(int)
print(f'float: {float}')
print(f'octal: {octal}')
print(f'hex: {hex}')
