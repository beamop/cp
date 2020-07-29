def findDuplicate(nums):
    nums.sort()
    print(nums)

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]

print(findDuplicate([1,8,7,6,8,4]))
