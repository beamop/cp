def mergeTwoSortedList(list1, list2):
    sortedList = list1 + list2
    sortedList.sort()

    return sortedList

print(mergeTwoSortedList([1,2,3,4], [3,4,5,6]))