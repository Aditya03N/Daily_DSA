def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # only start from sequence beginning
        if num - 1 not in num_set:
            current = num
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)

    return longest

# Example
arr = [22, 23, 28, 24, 90]
print(longestConsecutive(arr))  # Output: 3

