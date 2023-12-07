#길이(mm)를 입력하면 inch로 환산하는 프로그램을 만들어보자(1mm = 0.039inch)

byInch = 0.039

length =  int(input('길이(mm) 입력: '))

result = length * byInch

print('{}mm => {}inch' .format(length, result))