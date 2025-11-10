
n = int(input())
a = list(map(int, input().split()))
ms = 0
cs = 0
for i in range(n):
   if a[i] == 0:
       cs += 1
   else:
       ms = max(ms, cs)
       cs = 0
print(max(ms, cs))
