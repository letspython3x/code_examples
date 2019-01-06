
# Question 2: checkPalindrome(s)

def palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return False


# Usage
s = 'MadaM'
if palindrome(s):
    print("String is a palindrome!")
else:
    print("String is not a palindrome!")
