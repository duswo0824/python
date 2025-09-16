# try 코드 안에서 여러개의 에러가 발생한 경우

# 1. 생겨난 예외마다 각기 다른 처리를 해주고 싶을 때
try:
    pass
except IndexError:
    pass
except KeyboardInterrupt:
    pass
except ValueError:
    pass

# 각 예외(에러 발생부분)마다 다른 처리 하나씩


# 2. 어떤 예외가 발생하던지 동일한 처리를 하고 싶을 때
try:
    pass
except Exception:
    pass
