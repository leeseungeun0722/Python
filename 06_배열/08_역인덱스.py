# 역인덱스를 사용하여 영어 점수를 오름차순과 내림차순으로 출력
# 영어 점수는 리스트로 구성한다

eng_score = [100,40,70,90,60]

eng_score.sort(reverse = True)

j = len(eng_score)
for i in eng_score:
    print(i,'(',-j,')', end='      ')
    j -= 1
# print(eng_score)

for a in range(-5,0):
    print(eng_score[a], a , end = '     ')