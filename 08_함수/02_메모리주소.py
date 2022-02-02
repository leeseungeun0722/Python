from unittest import result


def address_a():
    result = "붕어빵"
    result_adress = id(result)
    return result_adress

def address_b():
    result = "잉어빵"
    result_adress = id(result)
    return result_adress

print('a - result 변수의 메모리 주소 : ' ,address_a())
print('b - result 변수의 메모리 주소 : ' ,address_b())

