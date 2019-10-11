#import CH24_gameboards
import random
print("PLAYER 1 : X")
print("PLAYER 2 : O")
row1=[]
row2=[]
row3=[]

gameover=False

a=['X','O','_']

a1=random.choice(a)
row1.append(a1)
a2=random.choice(a)
row1.append(a2)
a3=random.choice(a)
row1.append(a3)
b1=random.choice(a)
row2.append(b1)
b2=random.choice(a)
row2.append(b2)
b3=random.choice(a)
row2.append(b3)
c1=random.choice(a)
row3.append(c1)
c2=random.choice(a)
row3.append(c2)
c3=random.choice(a)
row3.append(c3)

join1="   ".join(row1)
join2="   ".join(row2)
join3="   ".join(row3)

def displayBoard():
    print(join1)
    print("\n")
    print(join2)
    print("\n")
    print(join3)
    print("\n")

displayBoard()

def condition():
    if a1==a2 and a1==a3 :
        if a1=='X':
            print("PLAYER 1 IS WINNER")
        elif a1=='O':
            print("PLAYER 2 IS WINNER")
            
    elif a1==b1 and a1==c1:
        if b1=='X':
            print("PLAYER 1 IS WINNER")
        elif b1=='O':
            print("PLAYER 2 IS WINNER")
        
    elif a1==b2 and a1==c3:
        if b2=='X':
            print("PLAYER 1 IS WINNER")
        elif b2=='O':
            print("PLAYER 2 IS WINNER")
        
    elif b1==b2 and b1==b3:
        if b1=='X':
            print("PLAYER 1 IS WINNER")
        elif b1=='O':
            print("PLAYER 2 IS WINNER")
        
    elif c1==c2 and c1==c3:
        if c1=='X':
            print("PLAYER 1 IS WINNER")
        elif c1=='O':
            print("PLAYER 2 IS WINNER")
        
    elif b2==a2 and b2==c2:
        if b2=='X':
            print("PLAYER 1 IS WINNER")
        elif b2=='O':
            print("PLAYER 2 IS WINNER")
        
    elif a3==b3 and a3==c3:
        if c3=='X':
            print("PLAYER 1 IS WINNER")
        elif c3=='O':
            print("PLAYER 2 IS WINNER")
        
    elif c1==b2 and c1==a3:
        if c1=='X':
            print("PLAYER 1 IS WINNER")
        elif c1=='O':
            print("PLAYER 2 IS WINNER")
        
    else:
        print("GAME IS EITHER DRAW OR INCOMPLETE")

condition()
