#파이썬 문법중 is, == 연산자를 이용한 출력 결과를 설명하세요

#[1] : 숫자
a = 101
b = 100+1

print(a is b) #true
print(a == b) #true


#[2] : 문자열
c = 'korea'
d = 'korea'

print(c is d) #true
print(c == d) #true


g = 'korea!'
h = g[:-1]
print(c is h) #false

#분가한다! 다른 객체로 이동 =>슬라이스 하는 순간(=잘라내는 순간) 독립한다. 즉 새롭게 할당을 받는다 ! 


#[3] : 리스트
e = [1,2,3,4,5]
f =[1,2,3,4,5]

print(e is f)   #flase
print(e == f)   #true


# 숫자와 문자열은 같은 곳을 가르키고 있다. (기존에 있는 곳으로 간다)
# 리스트는 객체가 따로 만들어진다