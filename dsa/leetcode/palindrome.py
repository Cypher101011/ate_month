def isPalindrome(x):
    mystring = str(x)
    length = len(mystring)

    for i in range(length // 2):
        if mystring[i] != mystring[length - i - 1]:
            return False
    return True

x = input("Enter a number or string: ")
print(isPalindrome(x))
