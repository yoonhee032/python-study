#조합 계산 모듈을 만들고 다음 조합 계산 결과를 출력해보자

import combination as cb

numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))

result = int(cb.combinationCnt(numN, numR))
print(f'{numN}C{numR}: {result}')