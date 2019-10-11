import os,time
a1='_'
a2='_'
a3='_'
b1='_'
b2='_'
b3='_'
c1='_'
c2='_'
c3='_'

def condition():
    global g
    if (a1==a2 and a1==a3 and a1!='_') or (a1==b1 and a1==c1 and a1!='_') or (a1==b2 and a1==c3 and a1!='_'):
        if a1=='X':
            print("\n\n\t\t\tPLAYER 1 IS WINNER\n\n")
            g=1
            time.sleep(10)
        elif a1=='O':
            print("\n\n\t\t\tPLAYER 2 IS WINNER\n\n")
            g=1
            time.sleep(10)
    
    elif (b1==b2 and b1==b3 and b1!='_') or (b2==a2 and b2==c2 and b2!='_'):
        if b2=='X':
            print("\n\n\t\t\tPLAYER 1 IS WINNER\n\n")
            g=1
            time.sleep(10)
        elif b2=='O':
            print("\n\n\t\t\tPLAYER 2 IS WINNER\n\n")
            g=1
            time.sleep(10)

    elif (c1==c2 and c1==c3 and c1!='_') or (a3==b3 and a3==c3 and a3!='_'):
        if c3=='X':
            print("\n\n\t\t\tPLAYER 1 IS WINNER\n\n")
            g=1
            time.sleep(10)
        elif c3=='O':
            print("\n\n\t\t\tPLAYER 2 IS WINNER\n\n")
            g=1
            time.sleep(10)

    elif c1==b2 and c1==a3 and c1!='_':
        if c1=='X':
            print("\n\n\t\t\tPLAYER 1 IS WINNER\n\n")
            g=1
            time.sleep(10)
        elif c1=='O':
            print("\n\n\t\t\tPLAYER 2 IS WINNER\n\n")
            g=1
            time.sleep(10)

    elif (a1!='_' and a2!='_' and a3!='_' and b1!='_' and b2!='_' and b3!='_' and c1!='_' and c2!='_' and c3!='_'):
        print("GAME DRAW")
        g=-1
        time.sleep(10)

def board():
    print('''              ------ ------ ------
             |      |      |      |
             |  {}   |  {}   |  {}   |
             |      |      |      |
              ------ ------ ------
             |      |      |      |
             |  {}   |  {}   |  {}   |
             |      |      |      |
              ------ ------ ------
             |      |      |      |
             |  {}   |  {}   |  {}   |
             |      |      |      |
              ------ ------ ------ '''.format(a1,a2,a3,b1,b2,b3,c1,c2,c3))

p=0
i=0
def condition2(x):
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    global i
    if x==1:
        if a1=='_':
            a1=p
        else :
            print("YOU TRIED TO FILL ALREADY FILLED CELL")
            i=i-1
                
    elif x==2:
        if a2=='_':
            a2=p
        else :
            print("YOU TRIED TO FILL ALREADY FILLED CELL")
            i=i-1
                
    elif x==3:
        if a3=='_':
            a3=p
        else :
            print("YOU TRIED TO FILL ALREADY FILLED CELL")
            i=i-1
                
    elif x==4:
        if b1=='_':
            b1=p
        else :
            print("YOU TRIED TO FILL ALREADY FILLED CELL")
            i=i-1
                
    elif x==5:
        if b2=='_':
            b2=p
        else :
            print("YOU TRIED TO FILL ALREADY FILLED CELL")
            i=i-1
                
    elif x==6:
        if b3=='_':
            b3=p
        else :
            print("YOU TRIED TO FILL ALREADY FILLED CELL")
            i=i-1
                
    elif x==7:
        if c1=='_':
            c1=p
        else :
            print("YOU TRIED TO FILL ALREADY FILLED CELL")
            i=i-1
                
    elif x==8:
        if c2=='_':
            c2=p
        else :
            print("YOU TRIED TO FILL ALREADY FILLED CELL")
            i=i-1
                
    elif x==9:
        if c3=='_':
            c3=p
        else :
            print("YOU TRIED TO FILL ALREADY FILLED CELL")
            i=i-1
                

board()
print("PLAYER 1 TURN.....")
x=int(input("choose where u want to draw : "))
i=0
g=0
while g==0:
    os.system('cls')
    if i%2==0:
        p='X'
        condition2(x)
    elif (i%2)!=0 :
        p='O'
        condition2(x)
    i=i+1
    board()
    condition()
    if g==0:
        if i%2==0:
            print("PLAYER 1 TURN.....")
        elif i%2==1:
            print("PLAYER 2 TURN.....")
        x=int(input("choose where u want to draw : "))
    

