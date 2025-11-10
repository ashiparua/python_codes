# Negative integer
A = list(map(int,input().split()))
res=[]
for i in range(len(A)):
    if A[i] < 0:
        res.append(A[i])
print(res)