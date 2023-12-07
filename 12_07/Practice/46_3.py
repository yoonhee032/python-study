#중간, 기말고사 점수를 입력하면 총점과 평균이 출력되는 프로그램 만들기.

middleScore = input('중간 고사 점수: ')
finalScore = input('기말 고사 점수: ')

if(middleScore.isdigit() and finalScore.isdigit()):
    middleScore = int(middleScore)
    finalScore = int(finalScore)

    totalScore = middleScore + finalScore
    avg = (middleScore + finalScore) / 2

    print('총점 : {} , 평균 : {}' .format(totalScore, avg))

else:
    print('잘못 입력했습니다.')

