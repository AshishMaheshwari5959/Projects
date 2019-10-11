x=int(input("ENTER THE NUMBER U SELECTED : "))
a=list(range(1,100))
j=1
for i in a :
    while i!=x:
        i=a[int(len(a)/2)]
        print(i)
        if i==x:
            print("u got me")
            break
        if i<x:
            print("LOW")
            del a[:int(len(a)/2)]
            j=j+1
        if i>x:
            print("HIGH")
            del a[int(len(a)/2):]
            j=j+1
    if i==x:
        break
print(" YOU GUESSED IN {} CHANCES".format(j))
