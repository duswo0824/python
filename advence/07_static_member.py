class Robot:
    # 멤버 변수
    count = 0

    #멤버 함수 #self 현재 이 객체라는 의미
    def how_count(self):
        print(f'객체 메서드 : {self.count}')

    @classmethod # 원본 영역의 변수를 건드릴 수 있다는 표시
    def std_count(self):
        print(f'클래스 메서드 : {self.count}')

# 두개의 다른 복사본 즉, r1을 건드려도 r2는 영향 받지 않음
r1 = Robot()
r2= Robot()
# r1과 r2는 서로 다른 객체이므로 count 를 건드렸을 때 서로 영향 받지 않는다.
r1.count += 1
print(f'r1.count : {r1.count}') # 1
print(f'r2.count : {r2.count}') # 0
r2.count = 100
print(f'r1.count : {r1.count}') # 1
print(f'r2.count : {r2.count}') # 100

# 원본의 내용을 고치고 싶다면? 원본으로 직접 가서 고쳐야 한다. # 원본 : Robot
Robot.count = 1000

# 원본(static)영역에서 고쳤을때 당연히 복사본(heap)영역에는 영향이 없다.
print(f'r1.count : {r1.count}')
print(f'r2.count : {r2.count}')
r1.how_count()
r2.how_count()

# 마찬가지로 원본의 내용을 확인하고 싶다면 원본영역으로 가서 확인해야 한다.
print(f'원본 count : {Robot.count}')
# 멤버 함수는 self라는 객체를 항상 가지고 있는데 원본은 복사한 것이 아니기 때문에 객체가 없음
#@classmethod # 원본 영역의 변수를 건드릴 수 있다는 표시를 넣어주면 실행가능
Robot.std_count() #Robot.std_count() missing 1 required positional argument: 'self'
