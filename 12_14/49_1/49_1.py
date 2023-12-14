#순열 계산 모듈을 만들고 다음 순열 계산 결과를 출력해보자
#직접 구현
import permutation as pm
#
# numN = int(input('numN 입력 : '))
# numR = int(input('numR 입력 : '))

# print(f'{numN}P{numR} : {pm.getPermutationCnt(numN, numR , logPrint=False)}')

#모듈 이용
listVar = [1,2,3,4,5,7]
rVar = 3

pm.getPermutations(listVar, rVar)