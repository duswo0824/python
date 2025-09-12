# 함수선언(define)
def toaster(bread):
    print(f'{bread}이 구워지고 있다.') # 상황을 내눈에 보여주는 것
    return f'구워진{bread}' # 실제로 밖으로 보여지는 것

# 함수사용
dish = toaster('소금빵')
print(dish) # 나온 빵을 받을 접시가 필요하다

# 헷갈리는 내용 정리

def toaster(bread): # 선언 : 만들어만놨지 누가 사용한 건 아님
    print(f'{bread}이 구워지고 있다.') # 실질적 동작이 아님, 사람 눈에만 보이는 것
    return f'구워진{bread}' # 실제 밖으로 나오는 값

# 사용
toaster('베이글') # 그냥 이것만 하면 갈 곳이 없어짐 # 베이글이 구워지고 있다.

dish = toaster('베이글') #return으로 나온 값을 dish에 담는다.
print(dish) #dish 안의 값을 출력

print(toaster('크림빵')) #토스트기에서 나온 값을 바로 출력