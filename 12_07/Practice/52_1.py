#다음 내용을 참고하여 백신 접종 대상자를 구분하기 위한 프로그램을 만들어보자
# 의사코드 : 19세 이하 또는 65세 이상이면 출생 연도에 따른 접종
#           그렇지 않으면 하반기 일정 확인


age = int(input('나의 입력: '))
day = ''

if(age >= 65 or age <= 19):
    birthYear = int(input('출생 연도 끝자리 입력:'))
    if(birthYear == 1 or birthYear == 6):
      day = '월요일'
      print('{} 접종 가능!!' .format(day))
    elif(birthYear == 2 or birthYear == 7):
      day = '화요일'
      print('{} 접종 가능!!'.format(day))
    elif (birthYear == 3 or birthYear == 8):
      day = '수요일'
      print('{} 접종 가능!!'.format(day))
    elif (birthYear == 4 or birthYear == 9):
      day = '목요일'
      print('{} 접종 가능!!'.format(day))
    else:
      day = '금요일'
      print('{} 접종 가능!!'.format(day))

else:
    print('하반기 일정 확인하세요')