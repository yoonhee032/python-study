#1 ~ 100까지의 정수 중 십의자리와 일의자리에 대해 각각 홀/짝수를 구분하는 프로그램 만들기
for i in range(1, 101):

    if(i // 10 == 0):
        if (i % 2 != 0):
            print('[{}]: 홀수!'.format(i))
        else:
            print('[{}]: 짝수!'.format(i))
    else:
        num10 = i // 10
        num1 = i % 10

        if (num10 % 2 != 0) and (num1 == 0):
            print('[{}] 십의자리: 홀수!!, 일의자리: 0 ' .format(i))
        elif (num10 % 2 != 0) and (num1 % 2 != 0):
            print('[{}] 십의자리: 홀수!!, 일의자리: 홀수!! ' .format(i))
        elif  (num10 % 2 != 0) and (num1 % 2 == 0):
            print('[{}] 십의자리: 홀수!!, 일의자리: 짝수!! ' .format(i))
        elif (num10 % 2 == 0) and (num1 == 0):
            print('[{}] 십의자리: 짝수!!, 일의자리: 0 ' .format(i))
        elif (num10 % 2 == 0) and (num1 % 2 != 0):
            print('[{}] 십의자리: 짝수!!, 일의자리: 홀수!! ' .format(i))
        else:
            print('[{}] 십의자리: 짝수!!, 일의자리: 짝수!! ' .format(i))


