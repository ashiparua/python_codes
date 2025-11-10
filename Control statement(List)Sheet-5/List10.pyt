# 1 reverse method
l=[1,2,3,4,5]
l.reverse()
print(l)
# 2 reverse method
l=[1,2,3,4,]
ans=l[::-1]
print(ans)
# 3 reverse method
l=[1,2,3,4,5,6]
N=len(l)
for i in range(N//2):
    l[i],l[N-1-i]=l[N-1-i],l[i]
print(l)
# swaping method
a=3
b=5
a,b=b,a
print(a)
print(b)

    