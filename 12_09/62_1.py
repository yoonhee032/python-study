#집 앞 버스 정류장에서 학교까지 가는 버스 A,B,C의 운행정보가 다음과 같을 때,
#2대 이상의 버스가 정차하는 시간대를 출력해보자

busA = 15
busB = 13
busC = 8

totalMin = 60 * 17

for i in range(totalMin + 1):
    if i < 20 or i > (totalMin - 60):
        if i % busA == 0 and i % busB == 0:
            print('busA와 busB 동시 정차!', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{} : {}' .format(hour, min))
    else:
        if i % busA == 0 and i % busB == 0:
            print('busA와 busB 동시 정차!', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{} : {}'.format(hour, min))
        elif i % busA == 0 and i % busC == 0:
            print('busA와 busC 동시 정차!', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{} : {}'.format(hour, min))
        elif  i % busB == 0 and i % busC == 0:
            print('busB와 busC 동시 정차!', end='')
            hour = 6 + i // 60
            min = i % 60
            print('\t{} : {}'.format(hour, min))