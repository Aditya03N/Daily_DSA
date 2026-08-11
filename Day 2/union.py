a=[1,2,3,4,5]
b=[3,4,6,7]
n=len(a)
m=len(b)
result=[]
i=0
j=0
while i<n and j<m:
    if a[i]<b[j]:
     if not result or result[-1]!=a[i]:
        result.append(a[i])
        i+=1

    elif b[j]<a[i]:
        if not result or result[-1]!=b[j]:
           result.append(b[j])
           b+=1

    else:
        if not result or result[-1]!=a[i]:
           result.append(a[i])
           i+=1
           j+=1
while i<n:
       if not result or result[-1]!=a[i]:
           result.append(a[i])
           i+=1              

while j<m:
       if not result or result[-1]!=b[j]:
           result.append(b[j])
           j+=1                             

print(result)