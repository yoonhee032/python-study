#국어, 영어, 수학 점수 입력 후 총점 , 평균, 최저점수과목, 최고점수과목, 점수 차이를 각각 출력해보자

korean = int(input('국어 점수 입력: '))
english = int(input('영어 점수 입력: '))
math = int(input('수학 점수 입력: '))

total = korean + english + math
avg = total / 3

maxScore = korean
maxSubject = '국어'

if english > maxScore:
    maxScore = english
    maxSubject = '영어'

if math > maxScore:
    maxScore = math
    maxSubject = '수학'

minScore =  korean
minSubject = '국어'

if english < minScore:
    minScore = english
    minSubject = '영어'

if math < minScore:
    minScore = math
    minSubject = '수학'

print('총점: ', total )
print('평균: %.2f' % avg )
print("-" * 30)
print('최고 점수 과목(점수) : {}({})' .format(maxSubject, maxScore))
print('최저 점수 과목(점수) : {}({})' .format(minSubject, minScore))
print('최고, 최저 점수 차이 : {}' .format(maxScore - minScore) )