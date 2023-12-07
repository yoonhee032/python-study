#나의 나이가 100살이 되는 해의 연도를 구하는 프로그램을 만들어보자.

import datetime

today = datetime.datetime.today()

age = (input('나이 입력: '))

if age.isdigit():
    afterAge = 100 - int(age)
    afterYear = today.year + afterAge

    print('{}년 ({}년 후)에 100살!'.format(afterYear, afterAge))

else:
    print('잘못 입력했습니다.')