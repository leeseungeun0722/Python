# a = [ i, j for i in range(3) for j in range(3)]
# print(a)

# [1] : tuple로 묶어줘야 한다. 요소 각각으로 하면 에러가 난다

a = [(i,j) for i in range(3) for j in range(3)]
print(a)




# [2] : 이중 for문

# for i in range(3):
#     for j in range(3):

# => i j (0,0) (0,1) (0,2) (1,0) (1,1) (1,2)