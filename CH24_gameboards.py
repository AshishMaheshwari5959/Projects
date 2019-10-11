def cell():
    x=int(input("ENTER THE NUMBER OF ROWS YOU WANT : "))
    y=int(input("ENTER THE NUMBER OF COLUMNS YOU WANT : "))
    for i in range(x):
        print(" ------"*y)
        print("|      "*y,"|",sep='')
        print("|      "*y,"|",sep='')
        print("|      "*y,"|",sep='')
    print(" ------"*y)
cell()                
