# 리스트 요소의 값을 반복문을 사용하여 모두 출력하자
# 값을 모두 출력한 후에는 끝에 요소의 갯수를 함께 출력하자

lst = ['dog','hippo','elephant','lion','tiger','aligator']

n =0
for i in lst:
    print(i,end='   ')
    n += 1
print("총",n,'개 요소\n')

for j in range(len(lst)):
    print(lst[j], end='     ')
print('총',len(lst),'개 요소')
