def reverse(string):
    string=string[::-1]
    return string
x=str(input("ENTER A WORD TO CHECK PALINDROME\n"))
for c in x:
    print(c)
X=reverse(x)
if X==x:
    print("HURRAY IT IS A PALINDROME :)")
else:
    print("IT IS NOT A PALINDROME :(")
