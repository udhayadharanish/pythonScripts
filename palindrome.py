def palindrome(s):
    for i in range(len(s)):
        if(s[i] != s[len(s)-1-i]):
            return False
    return True
        

s = input("Enter the string: ")
print(palindrome(s))
