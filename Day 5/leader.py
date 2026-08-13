arr = [10, 22, 12, 3, 0, 6]
n=len(arr)
maxi=arr[n-1]
ans=[]
ans.append(maxi)
for i in range(n-2,-1,-1):
    if arr[i]>maxi:
        maxi=arr[i]
        print(maxi,end=" ")
        


