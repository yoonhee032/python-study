#원의 넓이와 둘레를 출력해보자

radius = int(input('반지름(cm) 입력 : '))
pi = 3.14

circleArea = (radius ** 2) * pi
circumference = radius * 2 * pi

print('원의 넓이 : %d' % circleArea )
print('원의 넓이 : %d' % circumference)
print('원의 넓이 : %.1f' % circleArea )
print('원 둘레길이 : %.1f' % circumference )
print('원의 넓이 : %.3f' % circleArea )
print('원 둘레길이 : %.3f' % circumference )