import random
def pick():
    f=open("sowpods.txt","r")
    x=random.randint(1,10000)
    for i , line in enumerate(f):
        if i==x:
            print(line.strip())
    f.close()












