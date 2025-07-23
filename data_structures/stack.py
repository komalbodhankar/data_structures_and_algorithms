# Example on how arrays work in python!
# Python's list has a default behavior of that of a stack!
class MyStack:
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0 

    def push(self, element: int, maxSize: int):
        if self.size == maxSize:
            print("Stack overflow")
            return
        self.size += 1
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            return
        self.size -= 1
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None 
        return self.stack[-1]
    
    def size(self):
        return self.size()
    
    def print(self):
        if self.isEmpty():
            print("Stack is empty")
        print(self.stack)


# Testing stack
stack = MyStack()

# Push elements upto maxSize
print("\nPushing elements into the stack")
stack.push(1, 3)
stack.push(2, 3)
stack.push(3, 3)

print("\nPrint the stack")
stack.print()

# Compute stack size
print("Size of the stack is: ", stack.size)

# Push element beyond maxSize
print("\nPush another element past maxlimit")
stack.push(4, 3)

# Pop all elements from stack
stack.pop()
stack.pop()
stack.pop()

# Validate if it is empty
print("\nPrint if stack is empty")
isEmpty = stack.isEmpty()
print(isEmpty)

# Try popping an empty stack
print("\nTry to pop an empty stack")
stack.pop()

