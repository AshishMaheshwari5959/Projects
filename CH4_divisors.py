num=int(input("enter any number "))
a=[]
for i in range(1,num,1):
    if num%i==0:
        a.append(i)
print("the list of divisors are")
print(a)
