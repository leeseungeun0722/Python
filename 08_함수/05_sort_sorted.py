# [1] : 리스트

lst = [1,2,30,20,100,44]

# [2] : sort() 함수를 이용한 오름차순, 내림차순 정렬
# sort()함수나 sorted() 함수나 아무런 옵션없이 사용하면 디폴트 정렬 => 오름차순
lst.sort()    # 오름차순
print(lst)
lst.sort(reverse=True)  # 먼저 오름차순으로 정렬이 되고나서 내림차순으로 정렬
print(lst)

# [3] : sorted() => 디폴드 값은 오름차순
list2 = sorted(lst)
print(list2)
#list2 = sorted(lst, reverse=True)

# 차이점 
# sorted => 원본배열은 lst는 그대로 유지 된다