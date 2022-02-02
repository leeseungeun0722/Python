#  for 문을 사용해서 4부터 21까지의 홀수들의 합을 구하는 코드

sum = 0
for i in range(4,22):
    if (i % 2 != 0):
        sum += i
print(sum)

f