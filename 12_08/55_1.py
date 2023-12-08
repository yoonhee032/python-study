#난수를 이용해서 가위, 바위, 보 게임을 만들어보자

import  random

comNum = random.randint(1,3)
comStatus = ''
selectStatus = ''

selectNum = int(input('가위, 바위, 보 선택 : 1.가위\t2.바위\t 3.보 '))

if comNum == 1 and selectNum == 2 or   \
    comNum == 2 and selectNum == 3 or \
    comNum == 3 and selectNum == 1:
        print('컴퓨터: 패, 유저: 승')
elif comNum == selectNum:
        print('무승부')
else:
    print('컴퓨터: 승, 유저: 패')

print('컴퓨터 : {}, 유저 : {}' .format(comNum, selectNum))