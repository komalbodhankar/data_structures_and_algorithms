def second_smallest_element(nums):
    smallest, ssmallest = float("inf"), float("inf")
    for num in nums:
        if num < smallest:
            ssmallest = smallest
            smallest = num
        elif ssmallest > num and num != ssmallest:
            ssmallest = num
        
    if ssmallest == float("inf"):
        return None
    return ssmallest

numbers1 = [-10,-9,-8,-17,-2,-23]
numbers2 = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
numbers3 = [2,1,3,4,5,6,7,-10,11,249]
print(f'Second smallest in numbers: {numbers1} is {second_smallest_element(numbers1)}')
print(f'Second smallest in numbers: {numbers2} is {second_smallest_element(numbers2)}')
print(f'Second smallest in numbers: {numbers3} is {second_smallest_element(numbers3)}')