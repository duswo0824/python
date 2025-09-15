# 인자값으로 아무것도 들어오지 않았을 경우 에러를 방지하기 위해 기본값 설정이 가능
def plus(num=0): #puls를 실행하면
    result = num + 5 # num이라는 인자값에 +5를하고
    return result # 반환하여 보여줌

print(plus(5)) # 10
# 아무 것도 넣지 않았을 때 대체할 수 있는 값 = 기본값 (num=0)을 넣으면 # 5
print(plus()) # plus() missing 1 required positional argument: 'num'