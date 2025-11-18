# Write a recursive function to find the factorial of a number. 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
N = int(input("enter the fact no."))
print(factorial(N))
