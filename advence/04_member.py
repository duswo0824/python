class Robot:

    # 생성자 : 객체화 할때 호출되는 함수의 일종으로 (init 초기화 : 최초의 값을 실행)
    #객체화가 될때 가장 먼저  호출된다.
    def __init__(self):
        print('Robot이 복사될 때 제일 먼저 호출되는 멤버')

    def doIt(self):
        print('나는 Robot의 함수 입니다.')

robot = Robot() # 객체화 했을때 생성자 __init__ 실행
robot.doIt() # 객체화된 robot으로 doit 함수 실행