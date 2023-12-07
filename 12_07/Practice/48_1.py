# 상품 가격과 지불 금액을 입력하면 거스름 돈을 계산하는 프로그램을 만들어보자
# 단, 거스름 돈은 지폐와 동전의 개수를 최소로 하고, 1원 단위 절사한다.


productPrice = int(input('상품 가격 입력 : '))
payPrice = int(input('지불 금액: '))

changeMoney =  ((payPrice - productPrice) // 10) * 10

print('거스름 돈 : {}(원단위 절사)' .format(changeMoney))

money50000 = changeMoney // 50000
changeMoney = changeMoney - (50000 * money50000)
money10000 = changeMoney // 10000
changeMoney = changeMoney - (10000 * money10000)
money5000 = changeMoney // 5000
changeMoney = changeMoney - (5000 * money5000)
money1000 = changeMoney // 1000
changeMoney = changeMoney - (1000 * money1000)
money500 = changeMoney // 500
changeMoney = changeMoney - (500 * money500)
money100 = changeMoney // 100
changeMoney = changeMoney - (100 * money100)
money10 = changeMoney // 10
changeMoney = changeMoney - (10 * money10)


print('-' * 30)
print('50,000 {}장' .format(money50000))
print('10,000 {}장' .format(money10000))
print('5,000 {}장' .format(money5000))
print('1,000 {}장' .format(money1000))
print('500 {}개' .format(money500))
print('100 {}개' .format(money100))
print('10 {}개' .format(money10))
print('-' * 30)