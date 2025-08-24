class MyQueue:
    def __init__(self):
        self.queue = []
        self.start = 0
        self.end = 0
    
    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, element: int, maxSize: int):
        if len(self.queue) == maxSize:
            return "Stack overflow"
        else:
            self.end += 1
            self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Stack underflow"
        else:
            self.queue.pop(0)
            
# When a Python file is run directly, the interpreter sets a built-in variable called __name__ to "__main__".
# So this condition: evaluates to True only if the file is being run directly (not imported as a module).
if __name__ == "__main__":
    queue = MyQueue()
    
    print("Enqueue elements into queue with maxSize 3...")
    queue.enqueue(1, 3)
    queue.enqueue(2, 3)
    queue.enqueue(3, 3)
    print(str(queue.queue) + "\n")

    print("Enqueue element beyond maxSize...")
    res = queue.enqueue(4, 3)
    print(str(res) + "\n")


    print("Dequeue elements from queue...")
    queue.dequeue()
    print(str(queue.queue))
    queue.dequeue()
    print(str(queue.queue))
    queue.dequeue()
    print(str(queue.queue) + "\n")


    print("Validate if queue is empty...")
    isEmpty = queue.isEmpty()
    print(str(isEmpty) + "\n")

    print("Try Dequeuing from an empty queue...")
    res2 = queue.dequeue()
    print(str(res2) + "\n")
