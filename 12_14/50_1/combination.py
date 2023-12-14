def combinationCnt(n, r):

    resultP = 1
    resultR = 1
    result = 1

    #순열 구하기
    for n in range(n, (n-r), -1):
        resultP  = resultP * n

    #팩토리얼 구하기
    for r in range(r, 0, -1):
        resultR = resultR * r

    #조합
        result = resultP / resultR


    return result