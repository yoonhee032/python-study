# def feeCalculator(i, w, e, g):
#     total = w + e + g
#     ratio = (total / i) * 100
#
#     print(f'공과금 : {total}원')
#     print(f'공과금 비율 : {ratio}%')

income = 0
waterPrice = 0; electricPrice = 0; gasPrice = 0

def setIncome(ic):
    global income
    income = ic

def getIncome():
    return income

def setWaterPrice(wp):
    global waterPrice
    waterPrice = wp

def getWaterPrice():
    return waterPrice

def setElectricPrice(ep):
    global electricPrice
    electricPrice = ep

def getElectricPrice():
    return electricPrice

def setGasPrice(gp):
    global gasPrice
    gasPrice = gp

def geGasPric():
    return gasPrice

def getUtiltyBill():
    result =  waterPrice + electricPrice + gasPrice
    return result

def getRatio():
    result = getUtiltyBill() / getIncome() * 100
    return result