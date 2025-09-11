cup = 0
running = True

while running :
    cup += 1 # += 더해서 대입 (cup + 1)
    print(cup)
    if cup == 10:
        #running = False
        break #cup이 10이 되면 종료
        
print('while 문 종료')