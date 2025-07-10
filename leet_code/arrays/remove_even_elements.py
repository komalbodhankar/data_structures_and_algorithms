def remove_even_elements(nums):
    return [num for num in nums if num % 2 != 0]

nums = [1,2,3,4,5,6,7,8,9]
print(f'Resultant array after removing even numbers from {nums} is: {remove_even_elements(nums)}')
