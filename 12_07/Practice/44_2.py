#다음 문장에서 특정 문자열의 위치를 찾아보기

article = ('파이썬(영어: Python)은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어로,'
        '플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적타이핑(dynamically typed)대화형 언어이다. '
        '파이썬이라는 이름은 귀도가 좋아하는 코미디 <Monty Python\'s Flying Circus에서 따온 것이다.')

strIdx = article.find('객체지향')
print('\'객체지향\' 문자열 위치 : ', strIdx)