# a,b 각각 변수에 들어가 있는 값을 교환하는 코드

#[1] : 변수 선언
a = 100
b = 200
print('교환전 : ', a,b)

#[2] : temp 변수를 이용한 swap
temp = a
a = b # 200
b = temp #100
print('교환후 : ' ,a,b)

#미리 변수에 저장 시켜놓는 것이다 (빼돌린다)