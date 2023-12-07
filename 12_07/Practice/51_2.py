#197개의 빵과 152개의 우유를 17명에게 동일하게 나눠준다고 할 때,
#한명의 학생이 갖게 되는 빵과 우유 개수를 구하고 남는 빵과 우유 개수를 출력하자

bread = 197
milk = 152
studentCnt = 17

breadInfo = divmod(bread, studentCnt)
milkInfo = divmod(milk, studentCnt)

print('학생 한명이 갖게되는 빵 개수 : {} ' .format(breadInfo[0]))
print('학생 한명이 갖게되는 빵 개수 : {}' .format(milkInfo[0]))
print('남는 빵 개수 : {}' .format(breadInfo[1]))
print('남는 우유 개수 : {}' .format(milkInfo[1]))