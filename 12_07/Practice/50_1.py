#시, 분, 초를 입력하면 초로 환산하는 프로그램을 만들어보자.

hour = int(input('시간 입력 : '))
min = int(input('분 입력 : '))
sec = int(input('초 입력 : '))

print('{}초' .format( format((hour*60*60) + (min*60) + sec , ',')))