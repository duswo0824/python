import oper

#dir() 내장함수를 사용하면 모듈에 정의되어 있는 변수, 함수 목록을 볼 수 있다.
print(dir(oper)) #_ _ 는 Pytion에서 만들어준 기본 속성

#모듈의 이름 확인
print(oper.__name__) # 특정 모듈의 이름을 확인 # oper
print(__name__) # 현재 나의 이름 -> 현재 실행되는 함수 #__main__(파이썬은 실행하면 메인)