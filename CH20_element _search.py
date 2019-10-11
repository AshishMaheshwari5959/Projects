a=[1,11,111,1111,2,22,222,2222]
a.sort()
print(a)
i=int(input(""))
'''for j in range(0,len(a)):
    if i==a[j]:
        print("yes the number exist")'''
if i in a:
    print("yes the number exist")
else:
    print("the number does not exist")
