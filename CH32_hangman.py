import random
f=open("sowpods.txt","r")
x=random.randint(1,10000)
for i , line in enumerate(f):
    if i==x:
        a=line.strip()
        #print(a)
f.close()
aa=list(a)
b=len(a)
#print(b)
h1='@'
h2='--'
h3='--'
h4='|'
h5='/'
h6="\ "
print("""       {}
     {}{}{}
      {} {}""".format(h1,h2,h4,h3,h5,h6))
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
        n=aa.index(g)
        aa[n]='0'
        p[n]=g
        print("you guessed right")
        print("""       {}
     {}{}{}
      {} {}""".format(h1,h2,h4,h3,h5,h6))
    else:
        print("oops you are wrong")
        i-=1
        z=z+1
        print("ONLY {} ATTEMPTS LEFT ".format(6-z))
        if z==1:
            h5=' '
        elif z==2:
            h5=h6=' '
        elif z==3:
            h2=h5=h6='  '
        elif z==4:
            h2=h3=h5=h6='  '
        elif z==5:
            h2=h3=h4=h5=h6=' '
        elif z==6:
            h1=h2=h3=h4=h5=h6=' '
        print("""       {}
     {}{}{}
      {} {}""".format(h1,h2,h4,h3,h5,h6))
        if z==6:
            print("YOU HAVE USED ALL YOUR ATTEMPTS")
            exit("you lost")
    i+=1
    jp=" ".join(p)
    print(jp)
print("you missed {} times".format(z)) 
