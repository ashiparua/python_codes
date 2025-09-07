N=int (input("enter the number"))
for i in range(1,N+1):
    for j in range(N-i+1):
        print("*",end=" ")
    for j in range(2*i-2):
        print(" ",end=" ")
    for j in range(N-i+1):
        print("*",end=" ")
    print()
