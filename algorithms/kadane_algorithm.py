'''
Kadane's Algorithm helps find maximum sublist sum in O(N) time complexity and O(1) space complexity
This algorithm uses bottom's-up approach of dynamic programming. 
'''
def kadane_algorithm_method1(numbers):
    if not numbers:
        return []
    
    curr_max = numbers[0]
    global_max = numbers[0]
    
    for i in range(1, len(numbers)):
        if curr_max < 0:
            curr_max = numbers[i]
        else:
            curr_max += numbers[i]
        
        if global_max < curr_max:
            global_max = curr_max
    return global_max

def kadane_algorithm_method2(numbers):
    curr_max = 0
    global_max = float("-inf")
    
    for number in numbers:
        curr_max = max(curr_max + number, number)
        global_max = max(curr_max, global_max)
    return global_max

if __name__ == "__main__":
    # Test cases
    numbers = [-2,1,-3,4,-1,2,1,-5,4]
    maxSum = kadane_algorithm_method1(numbers)
    print(f'Maximum sum of numbers={numbers} is: {maxSum} using method1')

    numbers = [-2,1,-3,4,1,-1,2,1,-3,4,-2,-5]
    maxSum = kadane_algorithm_method2(numbers)
    print(f'Maximum sum of numbers={numbers} is: {maxSum} using method2')