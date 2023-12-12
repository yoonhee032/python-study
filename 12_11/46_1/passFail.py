def passFail(s1, s2, s3, s4, s5):

    passAvgScore = 60; limitScore = 40

    def getTotal():
        total = s1 + s2 +s3 + s4 +s5
        print(f'총점 : {total}')
        return total

    def getAvg():
        avg = getTotal() / 5
        print(f'평균 : {avg}')
        return avg

    def printPassOrFail():
        print(f'{s1} : Pass') if s1 >= limitScore else print(f'{s1} : Fail')
        print(f'{s2} : Pass') if s2 >= limitScore else print(f'{s2} : Fail')
        print(f'{s3} : Pass') if s3 >= limitScore else print(f'{s3} : Fail')
        print(f'{s4} : Pass') if s4 >= limitScore else print(f'{s4} : Fail')
        print(f'{s5} : Pass') if s5 >= limitScore else print(f'{s5} : Fail')

    def printFinalPassOrFail():

        if getAvg() >= passAvgScore:
            if s1 >= limitScore and s2 >= limitScore and s3 >= limitScore and s4 >= limitScore and s5 >= limitScore:
                print('Final Pass!')
            else:
                print('Final Fail')
        else:
            print('Final Fail')

    getTotal()
    getAvg()
    printPassOrFail()
    printFinalPassOrFail()