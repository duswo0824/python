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

# wallk() 함수를 사용하기 위해 Person 클래스를 객체화한다.
p= Person()
p.walk()

# 상속 받은 Jumper와 Runner의 함수들을 내것처럼(p. 객체로부터) 사용한다.
# 상속 받으면 좋은 점 1. 객체 입장에서는 기능이 늘어난다.
# 상속 받으면 좋은 점 2. 사용자 입장에서는 하나의 객체화로 여러 기능을 사용할 수 있다.
p.run()
p.sprint()
p.jump()
p.high_jump()
