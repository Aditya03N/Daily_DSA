class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        j = 0  # position to place next non-zero

        for i in range(n):   # loop 0 se n tak chalega
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums

# Example
nums = [2,1]
sol = Solution()
print(sol.moveZeroes(nums))  # Output: [2,1]

