# 모듈에 함수까지 전부 불러와서 사용하는 방법
from com.py.oop.other_module import other_function
# com.py.oop 안에 있는 other_module의 other_function 을 사용하겠다.
other_function()

# 모듈을 불러와서 별칭을 주어서 사용하는 방법
from com.py.oop import other_module as mo # com.py.oop 안에 있는 other_module을 불러옴 (별칭 mo)
mo.other_function() #mo안에 있는 other_function 실행
