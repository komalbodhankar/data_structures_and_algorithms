def reverse_insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j>=0 and array[j] < key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
            
    return array

if __name__ == "__main__":
    array=[1,2,3,4,5]
    print(f"\nReverse insertion sort for array: {array}")
    result = reverse_insertion_sort(array)
    print(f"is: {result}")