
A = input("Enter a string: ")
B = int(input("Enter ASCII code: "))
char = chr(B)


if char in A:
    print(A.index(char))
else:
    print("Character not found")
