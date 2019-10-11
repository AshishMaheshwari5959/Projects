def reverse(string):
    string=string[::-1]
    return string
string=str(input("ENTER A SENTENCE : "))
spliting=string.split()
print(spliting)
reversing=reverse(spliting)
print(reversing)
joining=" ".join(reversing)
print(joining)
