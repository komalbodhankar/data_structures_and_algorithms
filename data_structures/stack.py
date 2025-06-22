# Example on how arrays work in python!
# Python's list has a default behavior of that of a stack!
def isStackEmpty(s: list):
    if len(s) == 0:
        return True
    else:
        return False

def push(s: list, element: int, maxSize: int):
    if len(s) == maxSize:
        return "Stack overflow"
    else:
        s.append(element)

def pop(s: list):
    if isStackEmpty(s):
        return "Stack underflow"
    else:
        s.pop()


# Testing stack
stack = []

# Push elements upto maxSize
push(stack, 1, 3)
push(stack, 2, 3)
push(stack, 3, 3)

print(stack)

# Push element beyond maxSize
res = push(stack, 4, 3)
print(res) # Stack overflow

# Pop all elements from stack
pop(stack)
pop(stack)
pop(stack)

# Validate if it is empty
isEmpty = isStackEmpty(stack)
print(isEmpty)

# Try popping an empty stack
res2 = pop(stack)
print(res2) # Stack underflow

