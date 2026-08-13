prefix_sum={}
max_len=0
curr_sum=0
arr=[2,0,0,3]
k=3

for i in range(len(arr)):
    curr_sum+=arr[i]
    if curr_sum==k :
        max_len=max(max_len,i+1)
    if curr_sum not in prefix_sum:
        prefix_sum[curr_sum]=i

    if (curr_sum-k) in prefix_sum:
        max_len=max(max_len,i-prefix_sum[curr_sum-k])
print(max_len)
# this is only for zeros