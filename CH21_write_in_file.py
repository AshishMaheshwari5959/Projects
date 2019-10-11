x=str(input("ENTER FILE NAME : "))
o=str(input("ENTER THE OPERATION : "))
f=open(x,o)
a=str(input("ENTER THE DATA U WANT TO ENTER IN A FILE\n"))
f.write(a)
while a!="end_of_file":
    a=str(input())
    if a!="end_of_file":
        f.write('''\n{}'''.format(a))
f=open(x,"r")
contents=f.read()
print(contents)
f.close()
