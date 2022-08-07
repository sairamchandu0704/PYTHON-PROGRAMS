print('\tMATRIX MULTIPLICATION\n')

r = int(input("Number of rows Matrix 1 : "))
c = int(input("Number of columns Matrix 1 : "))


print('''\nMATRIX 1 :''')
Matrix1 = [[] for vr in range(0, r)]
for vr in range(0, r):
    Matrix1[vr] = [0 for vc in range(0, c)]

for vr in range(0, r):
    for vc in range(0, c):
        Matrix1[vr][vc] = int(input())  

v = int(input("Number of columns For Matrix 2 : "))
print('''\nMATRIX 2 :''')
Matrix2 = [[] for vr in range(0, c)]
for vr in range(0, c):
    Matrix2[vr] = [0 for vc in range(0, v)]
for vr in range(0, c):
    for vc in range(0, v):
        Matrix2[vr][vc] = int(input())  

Product = [[] for vr in range(0, r)]                
for vr in range(0, r):
    Product[vr] = [0 for columns in range(v)]      
Products = 0          
for vv in range(0, v):
    for vr in range(0, r):
        for vc in range(0, c):
            Products += Matrix1[vr][vc] * Matrix2[vc][vv]
        Product[vr][vv] = Products
        Products = 0  

print('\nMatrix 1 : ', Matrix1)
print('\nMatrix 2 : ', Matrix2)
print('\nResult of Multiplication :', Product)