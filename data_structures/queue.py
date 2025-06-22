def isQueueEmpty(q: list):
    if len(q) == 0:
        return True
    else:
        return False
    

def enqueue(q: list, element: int, maxSize: int):
    if len(q) == maxSize:
        return "Stack overflow"
    else:
        q.append(element)

def dequeue(q: list):
    if isQueueEmpty(q):
        return "Stack underflow"
    else:
        q.pop(0)
        

# Testing queue
queue = []

enqueue(queue, 1, 3)
enqueue(queue, 2, 3)
enqueue(queue, 3, 3)

print(queue)

# Enqueue element beyond maxSize
res = enqueue(queue, 4, 3)
print(res)

# Dequeue elements from queue

dequeue(queue)
print(queue)
dequeue(queue)
print(queue)
dequeue(queue)
print(queue)


# Validate if queue is empty
isEmpty = isQueueEmpty(queue)
print(isEmpty)

# Try Dequeuing from an empty queue
res2 = dequeue(queue)
print(res2)
