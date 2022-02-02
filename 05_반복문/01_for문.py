# 0 ~ 9 까지 출력하는 for 반복문 예제

# [1] : for 반복문
 
for i in range(10):
    print(i)


# [2] 1 2 3 4 5 6 7 8 9 10 가로로 출력하기
for j in range(10):
    print(j, end='\t')

# [3] 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 가로로 출력하기

#n 변수로 지정 해도 된다. 

# n = 0
for a in range(10):
    if a < 9 :  #n < 9:
        print(a, end =' , ')
    else:
        print(a)
    # n += 1