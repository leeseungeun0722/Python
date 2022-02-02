# 학생들의 영어 점수를 오름차순으로 출력
# 영어 점수는 리스트로 구성한다
# 내림차순도 구현해본다

eng_score = [40,100,70,90,60]

# [1] : sort() 또는 sorted()함수 사용 => 정렬은 디폴트가 오름차순
eng_score.sort()
print(eng_score)
eng_score.sort(reverse = True)
print(eng_score)


