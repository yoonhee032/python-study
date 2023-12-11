#다음과 같이 출력될 수 있도록 비행기 티켓 영수증 출력 함수를 만들어보자

childPrice = 18000
infantPrice = 25000
adultPrice = 50000
specialDc = 50

def formatedNumber(n):
    return format(n, ',')

def printAirRec(c1, c2, i1, i2, a1, a2):

    print("=" * 30)

    cp = c1 * childPrice
    cp_dc = int(c2 * childPrice * 0.5)
    print(f'유아 {c1}명 요금: {formatedNumber(cp)}원')
    print(f'유아 할인 대상 {c1}명 요금: {cp_dc}원')

    ip = i1 * infantPrice
    ip_dc = int(i2 * infantPrice * 0.5)
    print(f'유아 {i1}명 요금: {formatedNumber(ip)}원')
    print(f'유아 할인 대상 {i2}명 요금: {ip_dc}원')

    ap = a1 * adultPrice
    ap_dc = int(a2 * adultPrice * 0.5)
    print(f'유아 {a1}명 요금: {formatedNumber(ap)}원')
    print(f'유아 할인 대상 {a2}명 요금: {ap_dc}원')

    print("=" * 30)
    total = c1 + c2 + i1 + i2 + a1 + a2
    totalPrice = cp + cp_dc + ip + ip_dc + ap + ap_dc

    print(f'Total: {total}명')
    print('totalPrice : {}원' .format(formatedNumber(totalPrice)))


print('childPrice(24개월 미만)\t\t:18,000원')
print('infantPrice(만 12세 미만)\t\t:25,000원')
print('adultPrice(만 12세 이후)\t\t:50,000원')
print('국가 유공자 및 장애우 할인\t\t:50%')

childInput = int(input('유아 입력 : '))
childDiscountInput = int(input('할인 대상 유아 입력 : '))
infantInput = int(input('소아 입력 : '))
infantDiscountInput = int(input('할인 대상 소아 입력 : '))
adultInput = int(input('성인 입력 : '))
adultDiscountInput = int(input('성인 대상 유아 입력 : '))

printAirRec(childInput,childDiscountInput, infantInput, infantDiscountInput, adultInput, adultDiscountInput )






