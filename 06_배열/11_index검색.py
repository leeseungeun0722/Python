# 동물원에서 원하는 동물의 케이지를 찾아서 출력
# 이때 동물 이름은 사용자 입력으로 처리
# 이문제는 리스트에서 원하는 특정 요소를 검색할 수 있는지 묻는 문제

animals = ['코끼리','사자','악어','하마','원숭이']

# [1] : index() 사용하면 해당 리스트 요소 이름의 index 정보를 알아낼 수 있음

ani_input = input('케이지를 알고 싶은 동물 이름을 입력해주세요 :')
ani_index = animals.index(ani_input)
# print(ani_index)
print(f'{ani_input}동물의 케이지는 {ani_index}번 위치에 있습니다.{ani_index}번 케이지 약도를 출력하시겠습니까?')

#[2] : for문을 이용

# print("케이지를 알고 싶은 동물의 이름을 입력하세요 : ")
# a = input()

# for i in range(len(animals)):
#     if animals[i] == a :
#         print(a,"동물의 케이지는",i+1,"번 위치에 있습니다. ",i+1,"번 케이지 약도를 출력하시겠습니까 ?")
#     else:
#         i += 1
