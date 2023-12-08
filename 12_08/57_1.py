# 미세먼지수치에 따른 차량 운행 제한 프로그램을 만들어보자

import datetime

today = datetime.datetime.today()
day= today.day

dustyAmount = int(input('미세먼지 수치 입력: '))
carType = int(input('1.승용차\t2.영업용차\t'))
carNum = int(input('차량 번호 입력: '))
status = '금일 운행 가능합니다!!'

print('-' * 40)
print(today)
print('-' * 40)

if dustyAmount > 150 and carType == 1:
    if (day % 2) == (carNum % 2):
        print('차량 2부제 적용')
        print('차량 2부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')

if dustyAmount > 150 and carType == 2:
    if (day % 5) == (carNum % 5):
        print('차량 5부제 적용')
        print('차량 5부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')
if dustyAmount <= 150:
    if (day % 5) == (carNum % 5):
        print('차량 5부제 적용')
        print('차량 5부제로 금일 운행제한 대상 차량입니다.')
    else:
        print('금일 운행 가능합니다.')

print('-' * 40)