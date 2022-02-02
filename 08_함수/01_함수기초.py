# 기본적인 함수 호출

# ----------리턴값 X------------

# [1] : 함수작성

from cgitb import reset


def a():
    print("붕어빵")

def b():
    print("개구리빵")

# [2] : 함수호출

a()
b()


# ----------리턴값 O------------

#[1] : 함수작성

def c():
    result = '호랑이빵'
    return result

# [2] : 호출

print(c()) 