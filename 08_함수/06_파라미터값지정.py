# 함수 호출시 입력 파라미터 값을 지정하여 함수를 호출

def my_func(id,name,age):
    return id,name,age

a = input('input id    : ')
b = input('input name  : ')
c = input('input age   : ')

tuple_1 = my_func(a,b,c)

print(tuple_1,type(tuple_1))

# 따로출력, 타입도 str

d,e,f = my_func(id = 'batmen',name = '배트맨', age = '22')

print(d,e,f)