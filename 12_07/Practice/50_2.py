#금액, 이율, 거치기간을 받아 복리계산기를 만들어보자

money = int(input('금액 입력 : '))
interest = float(input('이율 입력: '))
year = int(input('기간 입력: '))

afterMoney = money

for i in range(year):
    afterMoney = afterMoney + (afterMoney * interest * 0.01)

afterMoneyFormated = format(int(afterMoney),',')

print('*' * 30)
print('이율 : %.1f' % interest)
print('원금 : {}원'  .format(format(money,',')))
print('{}년 후 금액 : {}원' .format(year, afterMoneyFormated))