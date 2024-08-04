s=input("enter your string: ")
def countletters(s):
    n=len(s)
    print("the string is: ",s)
    print("number of letters in the string is: ",n)
def capital(s):
    t=s.upper()
    print("The original string is:")
    print(s)
    print("The converted string is:")
    print(t)
def small(s):
    t=s.lower()
    print("The original string is:")
    print(s)
    print("The converted string is:")
    print(t)
def pali(s):
    n=len(s)
    c=" "
    for i in range(n-1,-1,-1):
        c=c+s[i]
    print(c)
    if s==c:
        print("entered string is a palindrome")
    else:
        print("entered string is  a not palindrome")
def repeat(s):
    t=int(input("how many times the string should repeat: "))
    v=s*t
    for i in range(0,len(v),len(s)):
        print(v[i:i+t-1])
def reverse(s):
    n=len(s)
    for i in range(n-1,-1,-1):
        print(s[i],end=" ")
def asccode(s):
    n=len(s)
    for i in range(0,n):
        print(s[i],":",ord(s[i]))
def vowelcount(s):
    c=0
    for i in s:
        if i=="A" or i=="E" or i=="I" or i=="O" or i=="U" or i=="e" or i=="a" or i=="i" or i=="o" or i=="u":
            c+=1
    print("number of vowel letters in the string is: ",c)        
op=1
while op!=8:
    print("1.countletters")
    print("2.capital")
    print("3.small")
    print("4.palindrome")
    print("5.repeat")
    print("6.reverse")
    print("7.ascii code")
    print("8.vowel count")
    print("9.quit")
    op=int(input("select the option which should perform: "))
    if op==1:
        countletters(s)
    elif op==2:
        capital(s)
    elif op==3:
        small(s)
    elif op==4:
        pali(s)
    elif op==5:
        repeat(s)
    elif op==6:
        reverse(s)
    elif op==7:
        asccode(s)
    elif op==8:
        vowelcount(s)
    
