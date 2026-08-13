# arr=[7,0,5,4,9]
# k=9
# sum=0
# for i in range (len(arr)):
#     for j in range(i,len(arr)):
       
#         if arr[i]+arr[j]==k:
#            print(i,j)


    # optimal is 
def two_sum(nums, target):
    seen = {}  # number -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
