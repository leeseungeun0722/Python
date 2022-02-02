# 1 ~ 100 까지의 수에서 짝수들만 출력하는 코드를 구현
# 두가지 방식으로 구현하자

first = 1
last = 100

#[1] : if문으로 2로 나눈 나머지가 0일 때 출력

for i in range(first, last+1):
    if(i % 2 == 0):
        print(i, end=' ')

print('\n\n')

#[2] : range()함수의 step(간격) 옵션 값을 이용하여 처리

for j in range(2,101,2):
    print(j, end=' ')

