import random

userNums = []; randNums = []; collNums = []
randBonNum = 0

#사용자가 입력한 숫자를 매개변수로 넘기면 userNums에 대입 될 수 있도록 하는 함수
def setUserNums(ns):
    global userNums
    userNums = ns

#사용자가 입력한 숫자를 빼오는 함수
def getUserNums():
    return userNums

#기계가 만든 숫자 세터
def setRandNums():
    global randNums
    randNums = random.sample(range(1, 46), 6)

#기계가 만든 숫자 게터
def getRandNums():
    return randNums

#보너스 숫자 세터 / 기존의 숫자와 겹치면 안됨
def setBonuNum():
    global randBonNum

    while True:
        randBonNum = random.randint(1, 45)
        if randBonNum not in randNums:
            break

#보너스 숫자 게터
def getBonuNum():
    return randBonNum

def lottoResult():
    global userNums
    global randNums
    global collNums

    collNums = []

    for un in userNums:
        if un in randNums:
            collNums.append(un)

    if len(collNums) == 6:
        print('1등 당첨')
        print(f'번호 : {collNums}')

    elif (len(collNums) == 5) and (randBonNum in userNums):
        print('2등 당첨')
        print(f'번호 : {collNums} , 보너스 번호 : {randBonNum}')

    elif len(collNums) == 5:
        print('3등 당첨')
        print(f'번호 : {collNums}')

    elif len(collNums) == 4:
        print('4등 당첨')
        print(f'번호 : {collNums}')

    elif len(collNums) == 3:
        print('5등 당첨')
        print(f'번호 : {collNums}')

    else:
        print('아쉽습니다. 다음 기회에')
        print(f'기계 번호: {randNums}')
        print(f'보너스 번호: {randBonNum}')
        print(f'선택 번호: {userNums}')
        print(f'일치 번호: {collNums}')

def startLotto():
    selectNums = []

    for i in range(6):
        userInput = int(input('번호(1~45)입력 : '))

        selectNums.append(userInput)

    setUserNums(selectNums)
    setRandNums()
    setBonuNum()

    lottoResult()
