# even,odd for array
a=list(map(int,input().split()))
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even numbers",even)
print("odd numbners:",odd)











