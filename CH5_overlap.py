a=[]
b=[]
print("ENTER THE ELEMENTS OF LIST ONE [TO STOP ENTER 999] ")
x=0
while x!=999:
    x=int(input())
    if x==999:
        break
    a.append(x)
print(a)
print("ENTER THE ELEMENTS OF LIST TWO [TO STOP ENTER 999] ")
x=0
while x!=999:
    x=int(input())
    if x==999:
        break
    b.append(x)
print(b)
c=[]
for i in a:
    for j in b:
        if i==j:
            c.append(i)
c=list(dict.fromkeys(c))
print("THE COMMON ELEMENTS OF THE TWO LISTS ARE")
print(c)
