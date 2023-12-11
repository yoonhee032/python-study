# 등차 수열의 n번째 값과 합을 출력하는 함수를 만들어보자.


def calc(n, d, g):
    number = 0
    sum = 0

    for i in range(g):

        number = n + (d * i)
        sum += number

        print(f'{i + 1}번째 항의 값 : {number}')
        print(f'{i + 1}번째 항까지의 합 : {sum}')


num = int(input('a1 입력: '))
distance = int(input('공차 입력: '))
goal = int(input('n 입력: '))


calc(num, distance, goal)
