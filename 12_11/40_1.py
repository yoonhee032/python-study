#산술 연산 계산기를 함수를 이용하여 만들어보자.

def calc():

    def calcSum(n1, n2):
        result = n1 + n2
        print(f'{n1} + {n2} = {result}')

    def calcSub(n1, n2):
        result = n1 - n2
        print(f'{n1} - {n2} = {result}')

    def calcMod(n1, n2):
        result = n1 * n2
        print(f'{n1} * {n2} = {result}')

    def calcDiv(n1, n2):
        result = n1 / n2
        print(f'{n1} / {n2} = {result}')

    def calcRemain(n1, n2):
        result = n1 % n2
        print(f'{n1} % {n2} = {result}')

    def calcQuo(n1, n2):
        result = n1 // n2
        print(f'{n1} // {n2} = {result}')

    def calcSqua(n1, n2):
        result = n1 ** n2
        print(f'{n1} ** {n2} = {result}')

    userInput1 = int(input('첫 번째 숫자 입력: '))
    userInput2 = int(input('두 번째 숫자 입력: '))

    if userSelect == 1:
        calcSum(userInput1, userInput2)
    elif userSelect == 2:
        calcSub(userInput1, userInput2)
    elif userSelect == 3:
        calcMod(userInput1, userInput2)
    elif userSelect == 4:
        calcDiv(userInput1, userInput2)
    elif userSelect == 5:
        calcRemain(userInput1, userInput2)
    elif userSelect == 6:
        calcQuo(userInput1, userInput2)
    elif userSelect == 7:
        calcSqua(userInput1, userInput2)


while True:
    print('-' * 30)
    userSelect = int(input('1. 덧셈, 2. 뺼셈, 3.곱셈, 4.나눗셈, 5.나머지, 6.몫, 7.제곱승 8. 종료 : '))
    if userSelect == 8:
        print('Bye~')
        break
    else:
        calc()




