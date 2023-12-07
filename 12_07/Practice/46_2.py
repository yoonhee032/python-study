#다음 코드에서 num1과 num2의 값을 서로 바꾸고 각각 출력하기

num1 = 10
num2 = 20
print('num1 : {}, num2 : {}' .format(num1, num2))

tempNum = num1
num1 = num2
num2 = tempNum
print('num1 : {}, num2 : {}' .format(num1, num2))