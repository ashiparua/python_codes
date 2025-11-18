# # Using recursion, print numbers from 1 to N. 
# def print_numbers(n):
#     if n == 0:
#         return
#     print_numbers(n - 1)
#     print(n, end=' ')
# N = int(input("enter the no."))
# print_numbers(N)
n=int(input("enter the number"))
def print1ton (n):
    if (n==0):
        return
    print1ton(n-1)
    print(n)
print1ton(n)
    