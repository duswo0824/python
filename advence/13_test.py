import traceback
# text = input('값을 넣으면 숫자로 변환 됩니다.')
# num = int(text)
# print(f'당신이 입력한 값 :{num} 이 숫자로 변환 되었습니다.')

# 1. 값을 넣으면 숫자로 변환 -> 숫자가 아닌 다른 문자를 넣었을 때 예외가 발생
# 2. 예외가 발생 했을 때 -> 예외에 대한 정보 출력 및 실행할 내용
# print (오류입니다)
#3. 다 끝났을 때 나타나는 문장

# try :
#     text = input('값을 넣으면 숫자로 변환 됩니다.')
#     num = int(text)
#     print(f'당신이 입력한 값 :{num} 이 숫자로 변환 되었습니다.')
# except ValueError as e:
#     traceback.print_exc()
#     print('오류입니다.')
# finally: # 되든 안되는 나타나는 값
#     print('====끝====')

# 제대로된 숫자가 입력되면 while 문 밖으로 나가게 함.
while True:
    try:
        text = input('값을 넣으면 숫자로 변환 됩니다.')
        num = int(text)
        print(f'당신이 입력한 값 : {num} 이 숫자로 변환 되었습니다.')
        break
    except ValueError:
        print(f'{text}는 숫자로 변환할 수 없는 값입니다.')

print('===끝===')


