b=[]
x=int(input("enter the element in a list to stop entering enter 999 \n"))
b.append(x)
while x!=999:
    x=int(input())
    if x==999:
        break
    b.append(x)
print(b)
B=[]
num=int(input("enter a number to see all number smaller than that "))
for i in b:
    if i<num:
        B.append(i)
print(B)
print("especially for you i have prepared a sorted list")
B.sort()
print(B)
