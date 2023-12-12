#구매 개수에 따라 할인율이 결정되는 모듈을 만들어 보자

import calculator as cl

if __name__ == '__main__':
    flag = True
    gs = []

    while flag:
        selectNum = int(input('1.구매, 2. 종료'))

        if selectNum == 1:
            goodsPrice = int(input('상품 가격 입력: '))
            gs.append(goodsPrice)

        elif selectNum == 2:
            result = cl.calculator(gs)
            flag = False

    print(f'할인율 : {result[0]}%')
    print(f'합계 : {cl.formatedNumber(result[1])}원')