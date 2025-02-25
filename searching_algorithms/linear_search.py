from sorting_algorithms.insertion_sort import insertion_sort
def linear_search(array, target):
    sortedArray = insertion_sort(array)
    for i in range(0, len(sortedArray)):
        if sortedArray[i] == target:
            return i

result = linear_search([2,3,4,11,-1,-4], 11)
print(result)