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
            

print("Enqueue elements into queue with maxSize 3...")
queue = MyQueue()

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
