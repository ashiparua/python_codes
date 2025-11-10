n=int(input())
a = list(map(int, input().split()))
d = 0
B = sum(a)
c = B/len(a)
for i in a:
   if i > c:
       d = d+1
print(d)


given an array and non negative numbers a of and non negative numbers b you need to find number of subarray in A with a sum>B

