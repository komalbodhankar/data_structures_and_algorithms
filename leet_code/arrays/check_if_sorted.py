def check_if_sorted(nums):
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            return False
    return True

nums = [1,2,3,4,5,5]
print(f'Is {nums} sorted? {check_if_sorted(nums)}')
nums = [-1,-1,-1,-1,-1,-1]
print(f'Is {nums} sorted? {check_if_sorted(nums)}')
nums = [248, 247, 246, 330, 7]
print(f'Is {nums} sorted? {check_if_sorted(nums)}')