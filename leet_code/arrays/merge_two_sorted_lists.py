def merge_two_sorted_lists(nums1: list, nums2: list):
    n = len(nums2)
    m = len(nums1)
    nums1 = nums1 + [0] * n
    
    end_idx = len(nums1) - 1
    
    while m > 0 and n > 0:
        if nums1[m-1] < nums2[n-1]:
            nums1[end_idx] = nums2[n-1]
            n -= 1
        else:
            nums1[end_idx] = nums1[m-1]
            m -= 1
        end_idx -= 1
        
    while n > 0:
        nums1[end_idx] = nums2[n-1]
        n -= 1
        end_idx -= 1
    
    return nums1

nums1 = [1,2,3]
nums2 = [4,5,6]

print(f'Merging two sorted arrays {nums1} and {nums2} is: {merge_two_sorted_lists(nums1, nums2)}')