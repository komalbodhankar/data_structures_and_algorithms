def remove_duplicates(nums):
    start = 0
    
    for curr in range(1, len(nums)):
        if nums[curr] != nums[start]:
            start += 1
            nums[start] = nums[curr]
    return start + 1 # Since indexes 0 - n-1 are filled with unique elements, n will be the size of unique elements. 

nums = [1,1,2,2,2,3,3]
print(f'Unique elements in this list {nums} is: {nums[:remove_duplicates(nums)]}')
