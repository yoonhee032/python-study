#아래 요금표를 참고해서 상수도 요금 계산기를 만들어보자.

userSelect = int(input('업종선택(1. 가정용\t2.대중탕용\t3.공업용):\t'))
userUseWater = int(input('사용량 입력: '))

print('=' * 30)

if userSelect == 1:
    waterFee = 540 * userUseWater
elif userSelect == 2:
    if userUseWater <= 50:
        waterFee = 820 * userUseWater
    elif userUseWater > 50 and userUseWater <= 300:
        waterFee = 1920 * userUseWater
    else:
        waterFee = 2400 * userUseWater
else:
    if userUseWater <= 500:
        waterFee = 240 * userUseWater
    else:
        waterFee = 470 * userUseWater

print('사용량\t\t: 요금')
print('{}\t\t: {}원' .format(userUseWater,format(waterFee, ','), ))