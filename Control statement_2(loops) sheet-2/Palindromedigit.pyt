a = int(input("Enter a number: "))
temp = a
rev = 0
while a > 0:
    digit = a % 10
    rev = rev * 10 + digit
    a = a // 10
if temp == rev:
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")