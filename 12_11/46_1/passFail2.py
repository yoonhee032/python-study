def passFail(*subject):

    passAvgScore = 60; limitScore = 40;

    def getTotal():
        total = 0
        for i in subject:
            total += i
        # print(f'총점 : {total}')
        return total

    def getAvg():
        avg = getTotal() / 5
        # print(f'평균 : {avg}')
        return avg

    def printPassOrFail():
        for i in subject:
            print(f'{i} : Pass') if i >= limitScore else print(f'{i} : Fail')


    def printFinalPassOrFail():

        for i in subject:
            flag = True
            if getAvg() >= passAvgScore:
                if i < limitScore:
                    flag = False
            else:
                flag = False
        if flag:
            print('Final Pass!')
        else:
            print('Final Fail')


    total = getTotal()
    avg = getAvg()

    print(f'총점 : {total}')
    print(f'평균 : {avg}')

    printPassOrFail()
    printFinalPassOrFail()