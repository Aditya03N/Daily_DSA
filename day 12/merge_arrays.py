# bruteforce solution o(n)+o(m+nlog(m+n))sorrrt ka
# nums1 = [-5, -2, 4, 5, 0, 0, 0]
# nums2 = [-3, 1, 8]
# n=len(nums1)
# m=len(nums2)
# k=n-m
# for i in range(m):
#     nums1[k+i]=nums2[i]
# nums1.sort()    
# print(nums1)    
nums1 = [-5, -2, 4, 5, 0, 0, 0]
nums2 = [-3, 1, 8]
m=4
n=3
i=m-1
j=n-1
k=m+n-1
while i>=1 and j>=1:
    if nums1[i]>nums2[j]:
        nums1[k]=nums1[i]
        i-=1

    else:
        nums1[k]=nums2[j]
        j-=1
    k-=1
while j>=1:
    nums1[k]=nums2[j]
    i-=1
    j-=1
print(nums1)            