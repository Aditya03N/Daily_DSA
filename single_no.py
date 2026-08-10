arr=[10,5,2,7,1,9]
max_length=0
curr_sum=0
for i in range(0,len(arr)):
    curr_sum+=arr[i]
    if curr_sum==15:
        max_length=max(max_length,i)
        curr_sum=0

print(max_length)        
    