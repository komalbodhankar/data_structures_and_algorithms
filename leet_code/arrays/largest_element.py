def largest_element(nums):
    largest = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > largest:
            largest = nums[i]
            
    return largest

nums = [-10, -9, -8, -17, -2, -23]
print(f'Largest in numbers: {nums} is {largest_element(nums)}')
nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
print(f'Largest in numbers: {nums} is {largest_element(nums)}')
nums = [2, 1, 3, 4, 5, 6, 7, -10, 11, 249]
print(f'Largest in numbers: {nums} is {largest_element(nums)}')