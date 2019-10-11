import random
print('''YOU ARE PLAYING COWS AND BULLS
         In this game u have to guess a four digit number if
         the digit is correct and at right place it says cow and if
         the digit is correct and at wrong place it says bull''')
x=random.randint(1000,9999)
print(x)
a=int(input("ENTER THE NUMBER U GUESSED : "))
def ones(p):
    return p%10
def tens(p):
    p=p/10
    p=p//1
    return p%10
def hundred(p):
    p=p/100
    p=p//1
    return p%10
def thousand(p):
    return p//1000
cow=0
bull=0
while cow!=4:
    cow=0
    bull=0
    if ones(x)==ones(a):
        cow=cow+1
    if tens(x)==tens(a):
        cow=cow+1
    if hundred(x)==hundred(a):
        cow=cow+1
    if thousand(x)==thousand(a):
        cow=cow+1
    if ones(a)==tens(x) or ones(x)==hundred(a) or ones(x)==thousand(a):
        bull=bull+1
    if tens(a)==ones(x) or tens(x)==hundred(a) or tens(x)==thousand(a):
        bull=bull+1
    if hundred(a)==tens(x) or hundred(x)==ones(a) or hundred(x)==thousand(a):
        bull=bull+1
    if thousand(a)==tens(x) or thousand(a)==hundred(x) or thousand(a)==ones(x):
        bull=bull+1
    print("THE COWS = {} THE BULLS = {}".format(cow,bull))
    if cow!=4:
        a=int(input("enter another number : "))
    if cow==4:
        print("YOU WON!!!!!!:):):):)")
