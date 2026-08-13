# nums = [-2,1,-3,4,-1,2,1,-5,4]
# sum=nums[0]
# curr_sum=0  
# for i in nums:
#    curr_sum+=i
#    if curr_sum<0:
#       curr_sum=0
#    else:   
#     curr_sum>sum
#     sum=curr_sum

# print(sum)   
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# max_sum = nums[0]
# curr_sum = 0  

# for i in nums:
#     curr_sum += i
#     if curr_sum < 0:
#         curr_sum = 0   # reset if sum goes negative
#     if curr_sum > max_sum:
#         max_sum = curr_sum   # update best sum

# print(max_sum)   # Output: 6 (subarray [4,-1,2,1])
nums = [-3, -2, -5 ,-3,-3,-4,2]

max_sum = float('-inf') 
print(max)  # -infinity
curr_sum = 0

for i in nums:
    curr_sum += i
    if curr_sum > max_sum:
        max_sum = curr_sum
    if curr_sum < 0:
        curr_sum = 0

print(max_sum)   # Output: -2
