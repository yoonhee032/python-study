#수입과 공과금을 입력하면 공과금 총액과 수입 대비 공과금 비율을 계산하는 모듈을 만들어보지
import calculator as cl

income = int(input('수입 입력 : '))
cl.setIncome(income)

waterMoney = int(input('수도요금 입력 : '))
cl.setWaterPrice(waterMoney)

elecMoney = int(input('전기요금 입력 : '))
cl.setElectricPrice(elecMoney)

gasMoney = int(input('가스요금 입력 : '))
cl.setGasPrice(gasMoney)

print(f'공과금 : {cl.getUtiltyBill()}')
print(f'공과금비율 : {cl.getRatio()}')




