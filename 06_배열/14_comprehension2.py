# [1] comprehension 괄호([])를 사용하지 않고 list()와  for문으로 1~10까지의 리스트를 만드시오
# [2] 1~10까지의 수를 comprehension 으로 각 숫자를 제곱한 값을 저장하는 리스트
# [3] 위 2번 문제에서 5의 제곱 값은 제외하고 출력
# [4] if 조건문을 사용하여 1~50 까지의 수에서 짝수 홀수 만 저장하는 리스트

# [1] : for문 + list() ==> 리스트 생성

list2 = list(i for i in range(1,11))
print(list2)

list1 = [i for i in range(1,11)]
print('[0] : ', list1)

a = []
for i in range(1,11):
    a.append(i)
print('[1] : ',a)



# [2] : 각 숫자를 제곱한 값

b = []
for j in range(1,11):
    b.append(j*j)
print('[2] : ',b)

# [2-1]

d = [i*i for i in range(1,11)] 
print('[2-1] : ',d)

list3 = [i**2 for i in range(1,11)]
print(list3)


#[3] : 5제곱 값 제외

list4 = [i*i for i in range(1,11) if i != 5]
print('list4 : ',list4)

c = []
for i in range(1,11):
    plus = i*i
    if plus != 5**2 :
        c.append(plus)
print('[3] : ',c)

# [4] : 홓수 짝수만 출력

list5 = [i for i in range(1,51) if i % 2 != 0]
print('list5 : ',list5)

e = []

for i in range(1,51):
    if i % 2 != 0:
        e.append(i)
print('홀수만 출력 : ',e)







    

