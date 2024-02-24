s=input("enter your string")
def countletters(s):
    c=0
    n=len(s)
    c=c+n
    print("number of letters in the string",c)
def capital(s):
    t=s.upper()
    print(t)
def small(s):
    t=s.lower()
    print(t)
def pali(s):
    n=len(s)
    c=" "
    for i in range(n-1,-1,-1):
        c=c+s[i]
    print(c)
    if s==c:
        print("entered string is not palindrome")
    else:
        print("entered string is  a palindrome")
def repeat(s):
    t=int(input("how many times the string should repeat"))
    print(s*t)
op=True
while op:
    print("1.countletters")
    print("2.capital")
    print("3.small")
    print("4.pali")
    print("5.repeat")
    print("6.quit")
    option=int(input("enter number of options"))
    if option==1:
        countletters(s)
    elif option==2:
        capital(s)
    elif option==3:
        small(s)
    elif option==4:
        pali(s)
    elif option==5:
        repeat(s)
    
        
        
        
