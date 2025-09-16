class Robot:
    # 멤버 변수
    count = 0

    #멤버 함수
    def how_count(self):
        print(f'객체 메서드 : {self.count}')

    def std_count(self):
        print(f'클래스 메서드 : {self.count}')
