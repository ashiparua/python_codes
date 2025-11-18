def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)
a, n = map(int, input("Enter x and n separated by space: ").split())
print("Result:", power(a, n))