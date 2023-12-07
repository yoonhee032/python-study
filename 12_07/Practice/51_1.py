#고도가 60m 올라갈때마다 기온이 0.8도 내려간다고 할 때 고도를 입력하면
#기온이 출력되는 프로그램을 만들어보자(지면온도 :29도)

bestTemp = 29
step = 60
stepTemp = 0.8

height = int(input('고도 입력 : '))

targetTemp = bestTemp - ((height // step) * 0.8)

if height % step != 0:
    targetTemp -= stepTemp

print('지면 온도 : {}' .format(bestTemp))
print('고도 %dm의 기온 : %.2f도' % (height, targetTemp))