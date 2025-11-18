def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
S = input("Enter a string: ")
if is_palindrome(S):
    print("Palindrome")
else:
    print("Not Palindrome")

    
    