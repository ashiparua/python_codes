# write a program to print n number fibonacci number
def fibonacci(n):
    if n <= 1:        
        return n
    return fibonacci(n-1) + fibonacci(n-2)   


num = int(input("enter the n fibonacci number:"))

print("Fibonacci Series:")
for i in range(num):
    print(fibonacci(i), end=" ")
    