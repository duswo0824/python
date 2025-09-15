# 인자값으로 아무것도 들어오지 않았을 경우 에러를 방지하기 위해 기본값 설정이 가능
def plus(num=0): #puls를 실행하면
    result = num + 5 # num이라는 인자값에 +5를하고
    return result # 반환하여 보여줌

print(plus(5)) # 10
# 아무 것도 넣지 않았을 때 대체할 수 있는 값 = 기본값 (num=0)을 넣으면 # 5
print(plus()) # plus() missing 1 required positional argument: 'num'

# *
# 인자값의 종류를 튜플(수정이 불가능한 List 형태)로만 받겠다.
def tuple_args(*numbers):
    print(numbers) # 튜플 형태로 반환
    total = 0
    for num in numbers:
        total += num
    return total # return은 무조건 함수 하나에 한번

# 이 방식은 사용자가 인자값의 갯수를 자유롭게 정해서 넣을 수 있다.
print(tuple_args(1, 2, 3, 4, 5))

# **
