num=int(input("enter the number"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print("_",end="")
    for j in range(0,i+1):
        print("*",end=" ")
    print()