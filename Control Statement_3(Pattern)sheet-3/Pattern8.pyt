N=int(input("Enter the number: "))
for i in range(N,0,-1):
    for j in range(0,N-i):
        print("_", end="")
    for j in range(0,i):
        print("*", end=" ")
    print()
