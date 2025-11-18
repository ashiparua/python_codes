# Using recursion, print numbers from N to 1. 

def print_reverse(n):
    if n == 0:
        return
    print(n, end=' ')
    print_reverse(n - 1)

N = int(input("enter the no."))
print_reverse(N)