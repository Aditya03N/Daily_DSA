# bruteforce
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         arr=[]
#         n=len(nums)
#         for i in range(n):
#           for j in range(i+1,n):
#             for k in range(j+1,n):
#              if i != j and i != k and j!=k and nums[i]+nums[j]+nums[k]==0:  
#                      triplet = sorted([nums[i], nums[j], nums[k]])
#                      if triplet not in arr:   # duplicate check
#                             arr.append(triplet)
#         return arr            

# hashing and 2ptr
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
      
#         n=len(nums)
#         set1=set()

#         k=0
#         for i in range(n):
#             s1=set()
#             for j in range(i+1,n):
#                 k=0
#                 k=-(nums[i]+nums[j])
#                 if k in s1:
#                     triplet=tuple(sorted([nums[i],nums[j],k]))
                  
#                     set1.add(triplet)
#                     s1.add(nums[j])
#                 else:
#                     s1.add(nums[j])      
#         result = [list(t) for t in set1]             
#         return result            

nums=[-1,0,1,2,-1,-4]

nums.sort()
arr=[]
for i in range(len(nums)):
 if i>0 and nums[i]==nums[i-1]:
   continue
 j=i+1
 k=len(nums)-1
 while k>j:
    if nums[i]+nums[j]+nums[k]==0:
      arr.append([nums[i],nums[j],nums[k]])
      j+=1
      k-=1
      while(j<k and nums[j]==nums[j-1]):
       j+=1
      while(j<k and nums[k]==nums[k+1]):
           k-=1   

    elif(nums[i]+nums[j]+nums[k]<0):
      j+=1

    else:
      k-=1        
print(arr)