#리스트 요소의 값을 반복문을 사용하여 거꾸로 출력시키자

lst = ['dog','hippo','elephant','lion','tiger','aligator']

for i in lst[::-1]:
    print(i, end='     ')
    