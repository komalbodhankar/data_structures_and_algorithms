# A linear search algorithm
'''
A stratergy where a single pointer starts at te beginning of an array shifting one index
   after the other until a target element is achieved. a.k.a sequential search/ simple search.
Works best when array is not sorted.
'''

def linear_search(array, target):
    numberOfTries = 0
    # When array is not sorted
    for i in range(0, len(array)):
        if array[i] == target:
            return numberOfTries
        numberOfTries+=1
    return -1 # Element was not found
        

result = linear_search([3,17,4,33,5,6,11], 10)
print(result)
