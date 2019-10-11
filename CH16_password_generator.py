import string
import random
capital=list(string.ascii_uppercase)
small=list(string.ascii_lowercase)
numbers=list(string.digits)
symbols=list(string.punctuation)
choice=str(input('''WHAT SHOULD IS THE STRENGTH OF YOUR PASSWORD :
                    STRONG : 12
                    MEDIUM : 10
                    WEAK :8
                    YOUR CHOICE : '''))

a=random.choices(capital,k=3)
#print(a)
b=random.choices(small,k=3)
#print(b)
c=random.choices(numbers,k=3)
#print(c)
d=random.choices(symbols,k=3)
#print(d)
if choice=='STRONG':
    x=a+b+c+d
    #print(x)
    random.shuffle(x)
    #print(x)
    joining="".join(x)
    print(joining)
if choice=='MEDIUM':
    x=a+b+c
    #print(x)
    random.shuffle(x)
    #print(x)
    joining="".join(x)
    print(joining)
if choice=='WEAK':
    x=a+c
    #print(x)
    random.shuffle(x)
    #print(x)
    joining="".join(x)
    print(joining)
