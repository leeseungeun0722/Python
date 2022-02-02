# for문을 사용하여 구구단 전체(2~9단)를 출력하는 코드
# 이문제는 이중 반복문을 사용할 수 있는지 묻는 문제

for i in range(2,10):
    for j in range(1,10):
        print(i,' X ',j,' = ',i*j)
    print('\n')