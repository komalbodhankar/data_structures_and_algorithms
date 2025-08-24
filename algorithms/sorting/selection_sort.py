'''
Selection sort algorithm

1. First find lowest element in A[1:n], swap that element with A[1]
2. Now find lowest element in A[2:n], swap that element with A[2]
3. And so on until all elements are sorted

Max time complexity: O(n^2) - best, average, and worst case
Max space complexity: O(1) - operates in constant space
'''
def selectionSort(array):
    for i in range(0, len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            while array[j] < array[min_idx]:
                min_idx = j
        # clever way to swap
        array[i] , array[min_idx] = array[min_idx], array[i]
    return array

if __name__ == "__main__":
    array=[7, 21, 3, 2, 0, -1, -30]
    print(f"\nSelection sort for array: {array}")
    result = selectionSort(array)
    print(f"is: {result}")