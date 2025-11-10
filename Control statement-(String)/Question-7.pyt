# given an array and non negative numbers a of and non negative numbers b you need to find number of subarray in A with a sum<B
# examples
#A=[2,3,5,6]
# B=10
A=[1,11,2,3,15]
B=10
count=0
N =len(A)
for i in range(0,N):
    sum=0
    for j in range(i,N):
        sum+=A[j]
        if(sum<B):
            count+=1
print(count)



