#사용자로부터 입력받으 개인정보를 출력해보자
#비밀번호와 주민번호 뒷자리는 '*'로 대체할 것

name = input('이름 입력 : ')
mail = input('메일 입력 : ')
id = input('아이디 입력 : ')
password = input('비밀번호 입력 : ')
firstNum = input('주민번호 앞자리 입력 : ')
secondNum =input('주민번호 뒷자리 입력 : ')
addr = input('주소 입력 : ')

pwStar = '*' * len(password)
secondNumStar = secondNum[0] + ('*' * 6)

print('-' * 30)
print(f'이름 : {name}')
print(f'메일 : {mail}')
print(f'아이디 : {id}')
print(f'비밀번호 : {pwStar}')
print(f'주민번호 : {firstNum} - {secondNumStar}')
print(f'주소 : {addr}')
