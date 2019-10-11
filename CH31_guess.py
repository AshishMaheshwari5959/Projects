import random
f=open("sowpods.txt","r")
x=random.randint(1,10000)
for i , line in enumerate(f):
    if i==x:
        a=line.strip()
        print(a)
f.close()
aa=list(a)
b=len(a)
print(b)
p=[]
for k in range(0,b):
    p.append('_')
j=" ".join(p)
print(j)
i=0
z=0
while i!=b:
    g=str(input("ENTER THE CHARACTER YOU GUESSED : "))
    if g in aa:
        for j in aa:
            idx=aa.index(j)
            print(idx)
        n=aa.index(g)
        aa[n]='0'
        p[n]=g
        print("you guessed right")
    else:
        print("oops you are wrong")
        i-=1
        z=z+1
    i+=1
    jp=" ".join(p)
    print(jp)
print("you missed {} times".format(z)) 
