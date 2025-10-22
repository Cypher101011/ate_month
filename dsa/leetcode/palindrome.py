
def isPalindrome(x):
    mystring=str(x)
    length=len(x)
    palindrome=False
    for i in range(len(x)):
        for j in range(len(x)):
            if mystring[i]==mystring[j]:
                print(mystring[i],mystring[j])
            
    return palindrome


x=input()
print(isPalindrome(x))

