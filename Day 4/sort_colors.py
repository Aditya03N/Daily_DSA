class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
     
        count1=0
        count0=0
        count2=0
        for i in range(len(nums)):
          if nums[i]==0:
              count0+=1
          elif nums[i]==1:
              count1+=1

          else:
              count2+=1
    
        index = 0
        for _ in range(count0):
            nums[index] = 0
            index += 1
        for _ in range(count1):
            nums[index] = 1
            index += 1
        for _ in range(count2):
            nums[index] = 2
            index += 1
        return nums                    
s1=Solution()
print(s1.sortColors([0,1,1,0,2,1,2]))