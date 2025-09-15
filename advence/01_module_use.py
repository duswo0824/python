# from 모듈 import 함수
# 사용할 함수를 미리 불러놓고 사용하는 방법
from oper import sum # oper의 파일에서(from) sum이라는 함수를 불러오겠다.(import)
print(f'sum() 함수 실행 : {sum(5,10)}')

# import 모듈
# 일단 모듈을 불러놓고 모듈로부터 원하는 함수를 사용하는 방법 #필요한 것만
import oper as op #as를 사용해서 이름줄임 (별칭)
print(f'minus() 함수 실행 : {op.minus(10,5)}') #op .(하위의) minus 함수

# 변수(v)도 불러다 사용할 수있다.
print(f'field 1 : {op.field1} / field 2 : {op.field2}')