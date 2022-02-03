def twoSum(nums, target):
    nums_hash = {}
    for index, value in enumerate(nums):
        potentialMatch = target - value
        if potentialMatch in nums_hash:
            return [nums_hash[potentialMatch], index]
        nums_hash[value] = index

# Removed ABS from the code because negative cases were getting cancelled
# if we have same number on different indexes, we need to return current index and index saved by the hash

nums = [3,3]
target = 6
ans = twoSum(nums,target)
print(ans)