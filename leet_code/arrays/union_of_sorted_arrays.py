'''
nums1 and nums2 are sorted.
'''
def union_of_sorted_array_bf(nums1, nums2):
    #bruteforce
    visited = set() # Maintain a set of unique nums present in both nums1 and nums2 -> space o(m + n)
    
    # Fill visited by iterating nums1 - o(mlogm) if m is the size of nums1
    for num in nums1:
        if num not in visited:
            visited.add(num)
    
    # Fill visited by iterating nums1 - o(nlogn) if n is the size of nums2
    for num in nums2:
        if num not in visited:
            visited.add(num)
    
    return list(visited) # o(m+n)

nums1 = [1,2,2,3,4,4,5]
nums2 = [2,3,3,4,5,5,6]
print(f'Union of nums1: {nums1} and nums2: {nums2} using brute-force approach is: {union_of_sorted_array_bf(nums1, nums2)}')


# 2-pointer approach
def union_of_sorted_array_optimal(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    i = 0
    j = 0
    union_arr = []
    
    '''
    Note: In python, the if conditions are executed from left to right, ensure to check if union_arr is empty before accessing its last element
    '''
    
    # Iterate through both nums array
    while i < n1 and j < n2:
        if (nums1[i] <= nums2[j]): # Pick the least value, and append it to resultant array
            if  len(union_arr) == 0 or union_arr[-1] != nums1[i]: # Ensure to check if the array already is present in the resultant array
                union_arr.append(nums1[i])
            i += 1
        else:
            # Do the same if element in nums2 is the least
            if len(union_arr) == 0 or union_arr[-1] != nums2[j]:
                union_arr.append(nums2[j])
            j += 1
    
    # If above while loop ends prematurely, or nums1 length is > nums2 length then iterate through rest of nums1 separately
    while i < n1:
        if len(union_arr) == 0 or union_arr[-1] != nums1[i]:
            union_arr.append(nums1[i])
        i += 1
    
     # If above while loop ends prematurely, or nums2 length is > nums1 length then iterate through rest of nums2 separately
    while j < n2:
        if len(union_arr) == 0 or union_arr[-1] != nums2[j]:
            union_arr.append(nums2[j])
        j += 1
            
    return union_arr

nums1 = [1,2,2,3,4,4,5]
nums2 = [2,3,3,4,5,5,6]
print(f'Union of nums1: {nums1} and nums2: {nums2} using optimal approach is: {union_of_sorted_array_optimal(nums1, nums2)}')