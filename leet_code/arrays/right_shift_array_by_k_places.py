def right_shift_array_by_k_places(nums, k):
    # If k is a multiple of len(nums), nums array will always get back to its original position. 
    k = k % len(nums) # Hence modulo
    
    # Reverse function that swaps nums within a given range of left and right, both inclusive
    def reverse(nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    '''
    Imagine we have the nums arrays as [1, 2, 3, 4, 5, 6]
    For left shift:
    - Initially reverse the entire array. Therefore nums will be [6, 5, 4, 3, 2, 1]
    - Now reverse all the elements from k to rest of k
        - Say k = 2
        - Then nums will be [6, 5, 1, 2, 3, 4]
    - Now reverse all the elements from 0 to k-1 to get thr resultant nums
        - Resultant nums will be [5, 6, 1, 2, 3, 4] <- Output
    '''
    reverse(nums, 0, len(nums)-1)
    reverse(nums, k, len(nums)-1)
    reverse(nums, 0, k-1)
    
    return nums

nums = [1,2,3,4,5,6]
k = 2
print(f'Right shifted array by {k} places is: {right_shift_array_by_k_places(nums, k)}')