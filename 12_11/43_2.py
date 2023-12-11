#다음과 같이 출력될 수 있도록 단리/월복리 계산기 함수를 만들어보자.

def formatedMoney(n):
    return format(n, ',')


def resultFormat(m, y, r, t):
    print('=' * 30)
    print(f'예치금\t : {m}원')
    print(f'예치기간\t : {y}년')
    print(f'연 이율\t : {r}%')
    print('-' * 30)
    print(f'{y}년 후 총 수령액 : {formatedMoney(t)}원')

def simpleInter(m , y, r):

    total = m + ((m * 0.01) * y * r)

    print('[단리 계산기]')
    resultFormat(m, y, r, int(total))

def compoundInter(m , y, r):

    year = y * 12
    rpm = (r / 12) * 0.01

    total = m

    for i in range(year):
        total = total + (total * rpm)

    print('\n[복리 계산기]')
    resultFormat(m, y, r, int(total))


money = int(input('예치금(원) : '))
year = int(input('기간(년): '))
yearRate = int(input('연 이율(년): '))

simpleInter(money, year, yearRate)
compoundInter(money, year, yearRate)
