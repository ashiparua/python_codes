n = int(input())
a = list(map(int, input().split()))
e = []
for i in range(n):
   if a[i] % 2 == 0:
       e.append(a[i])
if len(e) == 0:
   e.append(-1)
print(e)