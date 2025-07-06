def move_zeroes(nums):
    start = 0
    for curr in range(len(nums)):
        if nums[curr] != 0:
            nums[curr], nums[start] = nums[start], nums[curr]
            start += 1
    return nums

nums = [0,1,2,0,3,0,4,5,6,7,8,9,0]
print(f'If nums is {nums}, resultant array after moving all zeroes to the end is: {move_zeroes(nums)}')