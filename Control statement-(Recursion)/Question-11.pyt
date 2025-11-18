def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)
N = int(input("Enter a number: "))
print("Number of digits:", count_digits(abs(N)))