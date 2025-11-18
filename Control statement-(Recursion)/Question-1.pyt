# Recursion is a technic where a function calls itself directly or indirectly in order to solve a problem.
# In a recursion function the function makes one are more calls to itself as a part of its execution.
# The process continue until a base case is lead and which point the fuction stops calling itself and return are result.
# iterated method-:for loop use,complex solve 
# write a program to calculate sum of n natural number.
# n = int(input("Enter a natural number: "))
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print(sum)

def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    return n + sum_of_natural_numbers(n - 1)
N = int(input("Enter a number: "))
print("Sum of first", N, "natural numbers is:", sum_of_natural_numbers(N))
