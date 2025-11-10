# Add two list element

a1 =list(map(int, input().split()))
a2 = list(map(int, input().split()))
b = []
for i in range(len(a1)):
   b.append(a1[i] + a2[i])
print(b)
