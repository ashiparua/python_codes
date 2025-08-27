a = int(input("Enter a number: "))
sum = 0
for i in range(1, a + 1, 2):
    sum += i
print("Sum of odd numbers is", sum)