# class 이름 짓기 : 첫글자는 대문자, 특수문자 사용 X #예측 가능하게 만드는 것이 중요
# run() jump() walk() swim() -> 운동 exercise
# plus() minus() multiple() divide() -> 사칙연산 (계산) calculation
# acceleration() break() drift() -> 운전 drive

#Java 에서는 파일명 == 클래스명
#파이썬에서는 꼭 그렇지 않음.
class Student: #Student 라는 클래스(학생과 관련된 함수 및 변수가 들어오겠구나 라고 예측가능)
    pass # pass는 함수나 클래스에 아무것도 없을 때 오류방지를 위해 넣는 키워드

std1 = Student() #객체화해서 변수에 담은것 # Student()를 복사해서 std1에 담음
std2 = Student()
std3 = Student()
# 일련번호가 서로 다르다
# 파이썬에서도 객체화는 복사를 의미하므로 서로 다른 객체는 같지 않다.
print(std1)
print(std2)
print(std3)