class Parent():
    def __init__(self):
        print('부모 생성자 실행!')

class Child(Parent):
    def __init__(self):
        super().__init__() # 생략된 부모 생성자 # super : 부모를 의미
        print('자식생성자')

ch = Child()

# 부모가 초기화가 필요하다면 자식에게 값을 전달해서 자식이 부모에게 전달하도록 한다.
class SchoolMember: # 부모
    #멤버 필드
    name = ''
    age = 0

    def __init__(self, name, age): # 3. 받아온 값으로 초기화하고 객체화
        self.name = name # 현재 객체 name에 받아온 name을 넣어준다
        self.age = age

class Teacher(SchoolMember): # 자식
    salary = 0

    def __init__(self, name, age, salary):
        # super()를 이용해서 SchoolMember (부모)클래스를 호출
        super().__init__(name, age) # 2. 부모를 먼저 객체화 시키면서 초기화할 값 전달
        self.salary = salary # 4. 그리고 나서 내가 초기화 하면서 객체화

# 1. Teacher 라는 클래스를 t라는 변수에 객체화 (초기화를 위해 인자값 전달)
t= Teacher('김철수',33,50000000) #세개 다 찍어줘야함
# 5. namer 과 age는 부모 것이지만 내것처럼 내 객체에서 가져다 쓸 수 있게 됨
print(f'{t.name}({t.age})-{t.salary}')

#코드설명

# class SchoolMember: # 부모
#     #멤버 필드
#     name = ''
#     age = 0
#
#     def __init__(self, name, age): # 3. 받아온 값으로 초기화하고 객체화
#         self.name = name # 현재 객체 name에 받아온 name을 넣어준다
#         self.age = age
#
# class Teacher(SchoolMember): # 자식
#     salary = 0
#
#     def __init__(self, name, age, salary):
#         # super()를 이용해서 부모(SchoolMember)의 생성자(__init__)를 호출
#         super().__init__(name, age) # 2. 부모를 먼저 객체화 시키면서 초기화할 값 전달
#         self.salary = salary # 4. 그리고 나서 내가 초기화 하면서 객체화
#
# # 1. t라는 변수에 Teacher 라는 클래스를 객체화 (초기화를 위해 인자값 전달)
# t= Teacher('김철수',33,50000000) #세개 다 찍어줘야함
# # 5. namer 과 age는 부모 것이지만 내것처럼 내 객체에서 가져다 쓸 수 있게 됨
# print(f'{t.name}({t.age})-{t.salary}')
