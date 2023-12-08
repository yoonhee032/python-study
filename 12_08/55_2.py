#난수를 이용해서 홀/짝 게임을 만들어보자

import random

comNum = random.randint(1,2)
userSelect = int(input('홀/짝 선택 : 1.홀\t2.짝\t'))

result = ''
selectNum = ''

if comNum == userSelect:
    result = '성공'
else:
    result = '실패'

if comNum == 1:
    selectNum = '홀수'
else:
    selectNum = '짝수'

print('{}!! {}!!!' .format(result, selectNum))