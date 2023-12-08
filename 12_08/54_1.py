#국,영,수,사,과,국사 점수를 입력하면 각종 데이터가 출력되는 프로그램을 만들어보자

korAvg = 85; engAvg = 82; matAvg = 89; sciAvg = 75; hisAvg = 94
totalAvg = korAvg + engAvg + matAvg + sciAvg + hisAvg
avgAvg = int(totalAvg / 5)

kor = int(input('국어 점수 입력:' ))
eng = int(input('영어 점수 입력:' ))
math = int(input('수학 점수 입력:' ))
science = int(input('과학 점수 입력:' ))
history = int(input('국사 점수 입력:' ))

totalScore = kor + eng + math + science + history
avgScore = int(totalScore / 5)

korGap = kor - korAvg
engGap = eng - engAvg
mathGap  = math - matAvg
sciGap = science - sciAvg
hisGap = history - hisAvg
totalGap = totalScore - totalAvg
avgGap = avgScore - avgAvg

print('-' * 70)
print('총점 : {}({}), 평균 : {}({})' .format(totalScore, totalGap, avgScore, avgGap))
print('국어 : {}({}), 영어 : {}({}), 수학: : {}({}), 과학: : {}({}), 국사: : {}({})' .format(kor, korGap, eng, engGap, math, mathGap, science, sciGap, history, hisGap))
print('-' * 70)

str = '+' if korGap > 0 else '-'
print('국어 편차 : {}({})' .format(str * abs(korGap), korGap))
str = '+' if engGap > 0 else '-'
print('영어 편차 : {}({})' .format(str * abs(engGap), engGap))
str = '+' if mathGap > 0 else '-'
print('수학 편차 : {}({})' .format(str * abs(mathGap), mathGap))
str = '+' if sciGap > 0 else '-'
print('과학 편차 : {}({})' .format(str * abs(sciGap), sciGap))
str = '+' if hisGap > 0 else '-'
print('국사 편차 : {}({})' .format(str * abs(hisGap), hisGap))
str = '+' if totalGap > 0 else '-'
print('총점 편차 : {}({})' .format(str * abs(totalGap), totalGap))
str = '+' if avgGap > 0 else '-'
print('평균 편차 : {}({})' .format(str * abs(avgGap), avgGap))
