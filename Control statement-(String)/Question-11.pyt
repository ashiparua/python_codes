T = int(input("Enter number of strings:"))
for i in range(T):
    s = input("Enter string:")
    if s == s[::-1]:
        print(1)
    else:
        print(0)