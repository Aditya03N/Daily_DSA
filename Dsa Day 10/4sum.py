# nums=[2,2,2,2,2]
# n=len(nums)
# fourth=set()
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             for l in range(k+1,n):
#                 if nums[i]+nums[j]+nums[k]+nums[l]==8:
#                   quad=tuple(sorted([nums[i],nums[j],nums[k],nums[l]]))
#                   fourth.add(quad)

# result=[list(x) for x in fourth]
    
# print(result)                  

# better
nums=[1,0,-1,0,-2,2]
n=len(nums)
target=0
res=[]
nums.sort()
for i in range(n):
    if i>0 and nums[i]==nums[i-1]:
        continue
    for j in range(i+1,n-2):
       
        if j>i+1 and nums[j]==nums[j-1]:
            continue
        l=j+1
        r=n-1
        while l<r:
            if nums[i]+nums[j]+nums[r]+nums[l]==target:
                res.append([nums[i],nums[j],nums[r],nums[l]])
                l+=1
                r-=1
                while l<r and  nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r+1]:
                    r-=1
            elif nums[i]+nums[j]+nums[r]+nums[l]>target:
                r-=1
            else:
                l+=1          
print(res)