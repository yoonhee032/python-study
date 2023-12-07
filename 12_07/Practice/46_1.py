# 입력받은 체중과 키가 숫자이면 BMI를 계산하여 출력하기.

weight = input('체중 입력(g): ')
height = input('신장 입력(cm): ')

if weight.isdigit():
    weight = int(weight) / 10
if height.isdigit():
    height = int(height) / 100


bmi = weight / (height * height)

print('체중 : {}kg' .format(weight))
print('신장 : {}m' .format(height))
print('BMI : %.2f' % bmi)
