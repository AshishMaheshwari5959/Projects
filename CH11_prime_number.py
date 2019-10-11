def divisors() :
    num=int(input("enter any number "))
    a=[]
    for i in range(1,num+1,1):
        if num%i==0:
            a.append(i)
    print(a)
    return a
a=divisors()
x=len(a)
if x==2:
    print("IT IS A PRIME NUMBER")
elif 0<x<2:
    print("1 OR 0 IS NOT A PRIME NUMBER")
elif x==0:
    print("PLEASE ENTER POSITIVE NUMBER")
else:
    print("THE NUMBER IS NOT PRIME")
