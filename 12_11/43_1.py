#재귀함수를 이용해서 팩토리얼 함수를 만들어보자

def formatedNum(n):
    return format(n, ',')

def recursionFunc(n):

    if n == 1:
        return n

    return  n * recursionFunc(n-1)


userInput = int(input('input number : '))
print(formatedNum(recursionFunc(userInput)))