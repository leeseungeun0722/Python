#인덱스와 반복문을 사용하여 리스트 요소의 값들을 모두 출력

a = [100,200,300,400,500,[1,2,3],(4,5,6)]

j = 0
for i in a:
    print(j,' = ',i,end="        ")
    j += 1
