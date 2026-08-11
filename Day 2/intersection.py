a=[1,2,3,4,5]
b=[3,4,5,6,7]
n=len(a)
m=len(b)
i=0
j=0
result=[]
while i<n and j<m:
    if a[i]==b[j]:
        result.append(a[i])
        i+=1
        j+=1
    elif a[i]<b[j]:
        i+=1

    else:
        j+=1

print(result)                
