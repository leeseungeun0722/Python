# 리스트 컴프리헨션 이란 무엇인지 예제를 통해 설명
# list comprehension


# [1] : comprehension 
# => 이해력, 압축, 함축

# [2] : 수동으로 리스트 생성 

a = [1,2,3,4,5,6,7,8,9,10]
print('수동으로 리스트 생성 :',a,type(a))


# [3] : for 반복문 => append

b = []
for i in range(1,11):
    b.append(i)
print('자동으로 리스트 생성 :',b,type(b))

# [4] : list comprehension
c = [i for i in range(1,11)]
print('comprehension :' ,c)