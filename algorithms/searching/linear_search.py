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
        

if __name__ == "__main__":
    array = [3,17,4,33,5,6,11]
    print(f"Initialize an array: {array}")
    find_element = 10
    print(f"Find the element: {find_element}")
    result = linear_search(array, find_element)
    print(f"Return hops needed to find, else -1: {result}")
