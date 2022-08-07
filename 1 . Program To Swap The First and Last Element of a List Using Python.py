a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input())
    a.append(element)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("After Swaping First element with last result :")
print(a)
