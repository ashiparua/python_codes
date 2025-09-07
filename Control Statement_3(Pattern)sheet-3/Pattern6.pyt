N =5
for i in range(1,N+1):
    print("*",end="")
    for j in range(N+1-i):
        print("_",end=" ") 
    print("*",end=" ")
    print()