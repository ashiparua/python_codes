
n = int(input())
a = list(map(int, input().split()))
mx = a[0]
mn = a[0]
for i in a:
    if i > mx:
        mx = x
        if i < mn:
            mn = x
print(mx, mn)