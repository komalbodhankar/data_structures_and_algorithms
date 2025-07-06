def third_largest_element(nums):
    largest, slargest, tlargest = nums[0], float("-inf"), float("-inf")
    
    for i in range(len(nums)):
        if nums[i] > largest:
            tlargest = slargest
            slargest = largest
            largest = nums[i]
        elif slargest < nums[i] and nums[i] != largest and nums[i] != tlargest:
            tlargest = slargest
            slargest = nums[i]
        
        # If second largest does not exist, that means there is no third largest
        if slargest == float("-inf"):
            tlargest = None
    return tlargest

nums = [-10,-9,-8,-17,-2,-23]
print(f'Third largest in numbers: {nums} is {third_largest_element(nums)}')
nums = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
print(f'Third largest in numbers: {nums} is {third_largest_element(nums)}')
nums = numbers3 = [2,1,3,4,5,6,12,-10,11,249]
print(f'Third largest in numbers: {nums} is {third_largest_element(nums)}')