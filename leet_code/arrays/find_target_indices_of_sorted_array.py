'''
2089. Find Target Indices After Sorting Array

You are given a 0-indexed integer array nums and a target element target.
A target index is an index i such that nums[i] == target.
Return a list of the target indices of nums after sorting nums in non-decreasing order. 
If there are no target indices, return an empty list. 
The returned list must be sorted in increasing order.
'''

from typing import List
import sys
import os
sys.path.append(os.path.abspath('..'))

from algorithms.sorting.insertion_sort import insertion_sort


def targetIndices(nums: List[int], target: int) -> List[int]:
    sortedNums = insertion_sort(nums)
    targetIndices = []
    for i in range(0,len(sortedNums)):
        if sortedNums[i] == target:
            targetIndices.append(i)
    return targetIndices
result = targetIndices([1,2,5,2,3], 2)
noTarget = targetIndices([1,2,5,2,3], 7)
print(result)
print(noTarget)