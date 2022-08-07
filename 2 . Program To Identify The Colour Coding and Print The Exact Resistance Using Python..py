import math
print("Enter your Value For color\n","1.Red\n","2.Black\n","3.Brown\n","4.Orange\n","5.Yellow\n","6.Green\n","7.Blue\n","8.Grey\n","9.White\n")
a=int(input("Band 1 color = "))
b=int(input("Band 2 color = "))
c=int(input("Band 3 color = "))
def check(a):
    if a==2:
        return 0
    elif a==3:
        return 1
    elif a==1:
        return 2
    elif a==4:
        return 3
    elif a==5:
        return 4
    elif a==6:
        return 5
    elif a==7:
        return 6
    elif a==8:
        return 7
    elif a==8:
        return 8
    elif a==9:
        return 9
s=check(a)
v=check(b)
z=check(c)
print("The value of given register is\t:",s*10+v,"*10^{}".format(z))
print((s*10+v)*pow(10,z))
