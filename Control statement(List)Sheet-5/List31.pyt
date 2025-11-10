
n = int(input())
c = 0
for i in range(n):
    m, at = map(int, input().split())
    if m >= 75 and at >= 80:
        c += 1
print(c)