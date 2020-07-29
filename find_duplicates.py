def findDuplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return num
        seen[num] = True

print(findDuplicate([1,2,3,7,4,7,9,8,9,5]))
