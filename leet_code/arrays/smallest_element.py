def smallest_element(nums):
    smallest = float("inf")
    for num in nums:
        if num < smallest:
            smallest = num
            
    return smallest

nums = [-10, -9, -8, -17, -2, -23]
print(f'Smallest in numbers: {nums} is {smallest_element(nums)}')
nums = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
print(f'Smallest in numbers: {nums} is {smallest_element(nums)}')
nums = [2, 1, 3, 4, 5, 6, 7, -10, 11, 249]
print(f'Smallest in numbers: {nums} is {smallest_element(nums)}')