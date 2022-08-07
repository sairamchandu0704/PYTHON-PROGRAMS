import numpy as np
print('\tMATRIX MULTIPLICATION\n')

r = int(input("Number of rows Matrix 1 : "))
c = int(input("Number of columns Matrix 1 : "))


print('''\nMATRIX 1 :\t''')
Matrix1 = [[] for vr in range(0, r)]
for vr in range(0, r):
    Matrix1[vr] = [0 for vc in range(0, c)]

for vr in range(0, r):
    for vc in range(0, c):
        Matrix1[vr][vc] = int(input())  

v = int(input("Number of columns For Matrix 2 : "))
print('''\nMATRIX 2 :\t''')
Matrix2 = [[] for vr in range(0, c)]
for vr in range(0, c):
    Matrix2[vr] = [0 for vc in range(0, v)]
for vr in range(0, c):
    for vc in range(0, v):
        Matrix2[vr][vc] = int(input())  

print('\nMatrix 1 : ', Matrix1)
print('\nMatrix 2 : ', Matrix2)
print("Matrix Multiplication: ")

result = np.dot(Matrix1, Matrix2)
print(result)
