# 함수선언(define)
def toaster(bread):
    print(f'{bread}이 구워지고 있다.') # 상황을 내눈에 보여주는 것
    return f'구워진{bread}' # 실제로 밖으로 보여지는 것

# 함수사용
dish = toaster('소금빵')
print(dish) # 나온 빵을 받을 접시가 필요하다