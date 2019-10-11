import random
a=[1,2,3,4,5,6,7,8,9]
print("YOU ARE PLAYING A GUESSING GAME")
num=random.choice(a)
#print(num)
i=1
num2=int(input("ENTER A DIGIT TO GUESS WHICH NUMBER HAS COMPUTER SELECTED [ FROM 1-9 ] : "))
while num!=num2 :
    if num>num2:
        print("YOU GUESSED TOO LOW")
        num2=int(input("ENTER A DIGIT TO GUESS WHICH NUMBER HAS COMPUTER SELECTED [ FROM 1-9 ] : "))
    if num<num2:
        print("YOU GUESSED TOO HIGH")
        num2=int(input("ENTER A DIGIT TO GUESS WHICH NUMBER HAS COMPUTER SELECTED [ FROM 1-9 ] : "))
    if num==num2:
        print("YOU GUESSED EXACTLY RIGHT")
    i=i+1
print("YOU GUESSED {} NUMBER OF TIMES".format(i))
if i==1:
    print("YOU ARE EXCELLENT")
elif i<4:
    print("YOU ARE GOOD")
elif i<6:
    print("YOU ARE AVERAGE")
else :
    print("YOU ARE TOO BAD ")
