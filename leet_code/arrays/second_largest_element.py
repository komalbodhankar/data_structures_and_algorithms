def second_largest_element(nums):
    # Assume nums array has both +ve and -ve numbers
    largest, slargest = nums[0], float("-inf")
    for i in range(1, len(nums)):
        if nums[i] > largest:
            slargest = largest
            largest = nums[i]
        elif slargest < nums[i] and nums[i] != largest:
            slargest = nums[i]
    
    if slargest == float("-inf"):
        return None
    return slargest

numbers1 = [-10,-9,-8,-17,-2,-23]
numbers2 = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
numbers3 = [2,1,3,4,5,6,7,-10,11,249]
print(f'Second largest in numbers: {numbers1} is {second_largest_element(numbers1)}')
print(f'Second largest in numbers: {numbers2} is {second_largest_element(numbers2)}')
print(f'Second largest in numbers: {numbers3} is {second_largest_element(numbers3)}')
