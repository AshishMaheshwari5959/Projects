f1=open("prime.txt","w+")
f2=open("happy.txt","w+")
def prime(x):
    for i in range(1,x,1):
        fact=0
        for j in range(1,x,1):
            if i%j==0:
                fact=fact+1
        if fact==2:
            f1.write(str(i))
            f1.write("\n")
            
def numsquaresum(n):
    squaresum=0
    while n>0:
        squaresum=squaresum + (n%10)*(n%10)
        n=int(n/10)
    return squaresum

def ishappynumber(n):
    slow=n
    fast=n
    while slow!=1:
        slow=numsquaresum(slow)
        fast=numsquaresum(numsquaresum(fast))
        if slow!=fast:
            continue
        else:
            break
    return (slow==1)
    
def happy(x):
    for i in range(1,x,1):
        if ishappynumber(i)==True:
            f2.write(str(i))
            f2.write("\n")
prime(1000)
happy(1000)
f1.close()
f2.close()
f1=open("prime.txt","r")
f2=open("happy.txt","r")
prime_data=f1.read().splitlines()
happy_data=f2.read().splitlines()
for i in prime_data:
    if i in happy_data:
        print(i)
f1.close()
f2.close()

