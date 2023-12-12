#과목별 점수를 입력하면 합격 여부를 출력하는 모듈을 만들어보자

import passFail as pf

sub1 = int(input('과목1 점수 입력: '))
sub2 = int(input('과목2 점수 입력: '))
sub3 = int(input('과목3 점수 입력: '))
sub4 = int(input('과목4 점수 입력: '))
sub5 = int(input('과목5 점수 입력: '))

pf.passFail(sub1, sub2, sub3, sub4, sub5)
