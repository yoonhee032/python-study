#이동거리와 이동시간을 반환하는 함수를 만들어보자

def getDistanse(s, h, m):
   distance = 90 * (h + m /60)

   return distance


# 100:75 = 60:x --> x = 75 * 60 / 100
def getTime(s, d):
   time = d / s
   print(f'time : {time}')
   h = int(time)
   m = int((time - h) * 100 * 60 / 100)

   return[h, m]

print('-' * 60)
userSpeed = int(input('속도(km/h) 입력 : '))
userHour = int(input('시간(h) 입력 : '))
userMinute = int(input('시간(m) 입력 : '))

userDistance = getDistanse(userSpeed, userHour, userMinute)

print(f'{userSpeed}(km/h)속도로 {userHour}(h시간) {userMinute}(m)분 동안 이동한 거리: {userDistance}(km)')
print('-' * 60)

t = getTime(userSpeed, userDistance)
print(f'{userSpeed}km/h로 이동한 시간은 {t[0]}(h) 시간 {t[1]}(m) 분 입니다.')