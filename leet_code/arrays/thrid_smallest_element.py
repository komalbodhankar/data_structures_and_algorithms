def third_smallest_element(nums):
    smallest, ssmallest, tsmallest = float("inf"), float("inf"), float("inf")
    for i in range(len(nums)):
        if nums[i] < smallest:
            tsmallest = ssmallest
            ssmallest = smallest
            smallest = nums[i]
        elif ssmallest > nums[i] and nums[i] != smallest and nums[i] != tsmallest:
            tsmallest = ssmallest
            ssmallest = nums[i]
    if ssmallest == float("inf"):
        # Means that all elements in the array are same, therefore there will be no tsmallest
        tsmallest = None
    return tsmallest

nums = [-10,-9,-8,-17,-2,-23]
print(f'Third smallest in numbers: {nums} is {third_smallest_element(nums)}')
nums = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
print(f'Third smallest in numbers: {nums} is {third_smallest_element(nums)}')
nums = numbers3 = [2,1,3,4,5,6,12,-10,11,249]
print(f'Third smallest in numbers: {nums} is {third_smallest_element(nums)}')