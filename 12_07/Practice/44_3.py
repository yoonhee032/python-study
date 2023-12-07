# 사용자가 입력한 데이터를 모두 실수로 변경한 후 사각형, 삼각형의 넓이를 출력해보자


width = float(input('가로 길이 입력: '))
length = float(input('세로 길이 입력 : '))

print('-' * 30)
print('삼각형 넓이 : %f' % (width * length /2))
print('사각형 넓이 : %f' % (width * length))

print('삼각형 넓이 : %.2f' % (width * length /2))
print('사각형 넓이 : %.2f' % (width * length))
print('-' * 30)