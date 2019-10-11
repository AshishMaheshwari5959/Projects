print("This is a proagram to check if the given number is ODD or EVEN ")
n1=int(input("ENTER A NUMBER : "))
if n1%2==0:
    print("THE NUMBER {} IS EVEN".format(n1))
    if n1%4==0:
        print("THE NUMBER {} IS ALSO DIVISIBLE BY 4".format(n1))
    else:
        print("BUT THE NUMBER {} IS NOT DIVISIBLE BY 4".format(n1))
else:
    print("THE NUMBER {} IS ODD".format(n1))
n2=int(input("ENTER ANOTHER NUMBER TO CHECK FOR DIVISIBILITY : "))
D=int(input("ENTER THE NUMBER TO WHOM IT IS TO BE CHECKED : ")) 
if n2%D==0:
    print("THE NUMBER {} IS DIVISIBLE BY {}".format(n2,D))
else:
    print("THE NUMBER {} IS NOT DIVISIBLE BY {}".format(n2,D))
print("HURRAY CHALLENGE 2 IS COMPLETED")
