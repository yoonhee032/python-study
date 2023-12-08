#스마트 에어컨 상태가 자동으로 설정되는 프로그램을 만들어보자
indoorDegree = int(input('실내 온도 입력: '))
airStaus = ''

if indoorDegree <= 18:
    airStaus = 'OFF'
elif indoorDegree > 18 and indoorDegree <= 22:
    airStaus = '매우 약'
elif indoorDegree > 22 and indoorDegree <= 24:
    airStaus = '약'
elif indoorDegree > 24 and indoorDegree <= 26:
    airStaus = '중'
elif indoorDegree > 26 and indoorDegree <= 28:
    airStaus = '강'
else:
    airStaus = '매우 강'

print('에어컨 : {}!!' .format(airStaus) )