nums=[2,5,60,55]
temp=nums[0]
for i in range(1,len(nums)):
    nums[i-1]=nums[i]
nums[len(nums)-1]=temp
print(nums)
