# [1] : 딕셔너리 선언

dic = {}

# [2] : 데이터 입력

dic['id'] = 'hong'
dic['name'] = '홍길동'
dic['ex'] = [1,2,3,4]

# [3] : 데이터 출력

print(dic['id'])

# [4] : 반복문을 사용하여 출력
# key 값
for i in dic.keys():
     print(i)

# value 값
for i in dic.values():
    print(i)

# items
for i in dic.items():
    print(i)

# [5] : 중첩 딕셔너리 

dic1 = {
    'name' : '홍길동',
    'age' : 22,
    'dic2' : {
        'read' : 30,
        'sleep' : 40
    }
}

print('---'*10)
print(dic1['name'])
print(dic1['dic2'])
print(dic1['dic2']['sleep'])
print('---'*10)

# [6] : 삽입, 수정, 삭제

dic3 = {
    'name' : '이순신',
    'age' : 22
}

print('최초 : ',dic3)

dic3['id'] = 'lee'
print('삽입 : ',dic3)

dic3['id'] = 'kim'
print('수정 : ',dic3)

del dic3['id'] 
print('삭제 : ',dic3)