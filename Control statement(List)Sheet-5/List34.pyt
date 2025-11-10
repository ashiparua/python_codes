
n = int(input())
a = list(map(int, input().split()))
m = []
for i in a:
   if i%5==0:
       m.append(i)
m.reverse()
print(m)
