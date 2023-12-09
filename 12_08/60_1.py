#1부터 사용자가 입력한 정수까지의 합, 홀수의 합, 짝수의 합 그리고 팩토리얼을 출력하는 프로그램을 만들어보자

userNum = int(input('정수 입력: '))

sum = 0
oddSum = 0
evenSum = 0
facSum = 1

for i in range(1, userNum+1):
    sum += i
    facSum *= i
    if(i % 2 != 0):
        oddSum += i
    else:
        evenSum += i

print('합 결과 : {}'  .format(sum))
print('홀수 합 결과 : {}'  .format(oddSum))
print('짝수 합 결과 : {}'  .format(evenSum))
print('팩토리얼 결과 : {}'  .format(format(facSum, ',')))