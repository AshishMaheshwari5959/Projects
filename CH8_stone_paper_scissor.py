import random
print("YOU ARE PLAYING STONE, PAPER AND SCISSOR :):)")
name=str(input("ENTER YOUR NAME : "))
choice=str(input("ENTER YOUR CHOICE : "))
game=['STONE','PAPER','SCISSOR']
choice2=random.choice(game)
print("COMPUTER CHOOSES : {}".format(choice2))
if choice=="STONE":
    if choice2=="STONE":
        print("WOW IT'S A TIE :|:|")
    if choice2=="PAPER":
        print("SORRY YOU LOSE :(:(")
    if choice2=="SCISSOR":
        print("HURRAY YOU WON!!!! :):)")
if choice=="PAPER":
    if choice2=="PAPER":
        print("WOW IT'S A TIE :|:|")
    if choice2=="SCISSOR":
        print("SORRY YOU LOSE :(:(")
    if choice2=="STONE":
        print("HURRAY YOU WON!!!! :):)")
if choice=="SCISSOR":
    if choice2=="SCISSOR":
        print("WOW IT'S A TIE :|:|")
    if choice2=="STONE":
        print("SORRY YOU LOSE :(:(")
    if choice2=="PAPER":
        print("HURRAY YOU WON!!!! :):)")
again=str(input("TO PLAY AGAIN TYPE 'Y' OTHERWISE 'N' :"))
while again=='Y':
    choice=str(input("ENTER YOUR CHOICE : "))
    game=['STONE','PAPER','SCISSOR']
    choice2=random.choice(game)
    print("COMPUTER CHOOSES : {}".format(choice2))
    if choice=="STONE":
        if choice2=="STONE":
            print("WOW IT'S A TIE :|:|")
        if choice2=="PAPER":
            print("SORRY YOU LOSE :(:(")
        if choice2=="SCISSOR":
            print("HURRAY YOU WON!!!! :):)")
    if choice=="PAPER":
        if choice2=="PAPER":
            print("WOW IT'S A TIE :|:|")
        if choice2=="SCISSOR":
            print("SORRY YOU LOSE :(:(")
        if choice2=="STONE":
            print("HURRAY YOU WON!!!! :):)")
    if choice=="SCISSOR":
        if choice2=="SCISSOR":
            print("WOW IT'S A TIE :|:|")
        if choice2=="STONE":
            print("SORRY YOU LOSE :(:(")
        if choice2=="PAPER":
            print("HURRAY YOU WON!!!! :):)")
    again=str(input("TO PLAY AGAIN TYPE 'Y' OTHERWISE 'N' :"))
else:
    print("THANK YOU FOR PLAYING")
