# 학생들의 영어 점수 리스트에 새 전학생의 영어 점수를 추가해보자
# 추가외에도 수정, 삭제 리스트도 구현한다
# 이문제는 기존 리스트 또는 반리스트에 새로운 요소를 추가, 수정, 삭제하는 방법을 아는지 묻는 문제

# [1] : 원본
eng_scores = [90,60,75,100,88]
print("[1] 원본 :",eng_scores)

# [2] : 추가 => append() 사용.
eng_scores.append(99)
print("[2] 추가 :",eng_scores)

# [3] : 수정(변경) => index사용
eng_scores[-1] = 37
print("[3] 수정 :",eng_scores)

# [4] : 삭제 => remove
eng_scores.remove(37)
print("[4] 삭제 :",eng_scores)

# [4-1] : 삭제 =>del
del eng_scores[-1]
print("[4-1] 삭제 :",eng_scores)

 