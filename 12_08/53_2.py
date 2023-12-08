#문자 메시지 길이에 따라 문자 요금이 결정되는 프로그램을 만들어보자.

message = input('메시지 입력: ')
messageLimit = 50

if len(message) > messageLimit:
    print('MMS 발송!!')
    print('메시지 길이: {}' . format(len(message)))
    print('메시지 발송 요금 : 100원' )
else:
    print('SMS 발송!!')
    print('메시지 길이 : {}' .format(len(message)))
    print('메시지 발송 요금 : 50원')
