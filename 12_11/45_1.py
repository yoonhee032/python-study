#등비 수열의 n번째 값과 합을 출력하는 함수를 만들어보자


def calc(n1, r, g):

    valueN = 0
    sum = 0
    i = 1

    while i <= g:
        if i == 1:
            valueN = n1
            sum = valueN

            print(f'{i}번째 항의 값 : {valueN}')
            print(f'{i}번째 항까지의 합 : {sum}')

            i += 1
            continue

        else:
            valueN = valueN * r
            sum += valueN

            print(f'{i}번째 항의 값 : {valueN}')
            print(f'{i}번째 항까지의 합 : {sum}')

            i += 1



num = int(input('a1 입력: '))
distance = int(input('공비 입력: '))
goal = int(input('n 입력: '))


calc(num, distance, goal)