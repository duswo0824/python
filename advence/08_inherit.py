class Runner:
    # def __init__(self): # 생성자 생략
    #     pass
    def run(self): # 멤버함수
        print(f'달린다.') #f-string : 문자열만 할때는 사용 안해도 됨
    def sprint(self):
        print('전력질주를 한다.')

class Jumper:
    def jump(self):
        print('점프를 한다.')
    def high_jump(self):
        print('하이점프를 한다.')

class Person(Jumper, Runner): #Person 클래스가 Jumper와 Runner 를 상속받음
    def walk(self):
        print('걷는다.')


