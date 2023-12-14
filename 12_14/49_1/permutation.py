def getPermutationCnt(n, r, logPrint = True):

    result = 1

    for n in range(n , (n-r) , -1):
        if logPrint : print('n : {}'.format(n))
        result *= n

    return result

#모듈 이용
from itertools import permutations

def getPermutations(ns, r):

    pList = list(permutations(ns,r))

    print(f'{len(ns)}P{r} 개수 : {len(pList)}')

    for n in permutations(ns, r):
        print(n, end="")
