#PC에서 난수를 발생하면 사용자가 맞추는 게임을 만들어보자

import random

comNum = random.randint(1, 1000)
num = 0
flag = False

while (flag == False):
    num += 1
    userNum = int(input('1에서 1000까지의 정수 입력 : '))
    if(comNum == userNum):
        print("빙고")
        print('난수 : {}, 시도 횟수 : {}'.format(comNum, num))
        flag = True
    else:
        if comNum > userNum:
            print('난수가 크다!')
        else:
            print('난수가 작다!')

