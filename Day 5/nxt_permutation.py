nums=[3,2,1]
gola_index=-1
n=len(nums)

#
for i in range(n-1,0,-1):        
    if nums[i-1]<nums[i]:
     gola_index=i-1
     break

if gola_index == -1:
            nums[:] = nums[::-1]

else:
      swap_index=gola_index
      for j in range(n-1,gola_index,-1):
         if nums[j]>nums[gola_index]:
           swap_index=j
                  


      temp=nums[gola_index]
      nums[gola_index]=nums[swap_index]
      nums[swap_index]=temp

# Step 4: reverse suffix
      nums[gola_index+1:]=nums[gola_index+1:][::-1]
print(nums)