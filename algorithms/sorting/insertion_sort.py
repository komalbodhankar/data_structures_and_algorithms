def insertion_sort(array):
    '''
    Think of sorting cards.
    1. Initially, both hands are empty
    2. Pick a card using right hand and place in left, left hand is already sorted.
    3. Pick a card again and check if it is lower than the card in left hand, if so, 
       place it to the left of the left card, else to the right
    4. Continue to arrange cards by traversing from right to left
    5. Max time complexity: O(n^2). This is possible only if the array is a complete reverse of sorted.
    6. Max space complexity: O(1).
    '''
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j>= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
        
    return array

result = insertion_sort([167, 246, 30, 779, 833])
print(result)

result = insertion_sort([439, 294, 624, 44, 618])
print(result)

result = insertion_sort([769, 193, 787, 642, 651])
print(result)