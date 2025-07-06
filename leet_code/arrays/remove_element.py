'''
Return the slicing index of nums which does not contain the val
And print nums[:k]
'''
def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [3,1,2,3,4,5,3,6,7,3,8,3,9,3]
val = 3
print(f'Resultant array without {val} is: {nums[:remove_element(nums, val)]}')
