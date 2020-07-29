def pigeonHoleSort(nums):
    x = min(nums)
    y = max(nums)

    numOfHoles = y - x + 1

    holes = []
    for hole in range(0, numOfHoles):
        holes.append(0)


    for num in nums:
        holes[num - x] += 1

    sortedArr = []

    for count in range(numOfHoles):
        while holes[count] > 0:
            holes[count] -= 1

            sortedArr.append(count + x)

    return sortedArr

nums = [9,74,5,2,89,43]

print(pigeonHoleSort(nums))
