from random import randint
def matrix(n:int):
    mat = []
    for i in range(n):
        row = [randint(100, 999) for i in range(5)]
        mat.append(row)
    return mat
def new_matrix(mat1:list, mat2:list):
    my_matrix = []
    length = len(mat1)
    for i in range(length):
        row = []
        for j in range(length):
            if mat1[i][j] > mat2[i][j]:
                row.append(mat1[i][j])
            else:
                row.append(mat2[i][j])
        my_matrix.append(row)
    return my_matrix

mat1 = matrix(10)
mat2 = matrix(10)
for i in mat1:
    print(i)
print(50*'-')
for j in mat2:
    print(j)
print(50*'-')
for k in new_matrix(mat1, mat2):
    print(k)
