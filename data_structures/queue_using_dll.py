from doubly_linked_list import LinkedList as DoublyLinkedList
class MyQueue:
    def __init__(self):
        self.items = DoublyLinkedList()
    
    def isEmpty(self):
        return self.items.isEmpty()
    
    def start(self):
        if self.isEmpty():
            return None
        return self.items.get_head()
    
    def end(self):
        if self.isEmpty():
            return None
        return self.items.get_tail()
    
    def enqueue(self, element):
        return self.items.insert_at_tail(element)
    
    def dequeue(self):
        return self.items.delete_at_head()
        
    def size(self):
        length = 0
        if not self.isEmpty():
            curr = self.items.get_head()
            while curr:
                length += 1
                curr = curr.next
        return length
                
            

# When a Python file is run directly, the interpreter sets a built-in variable called __name__ to "__main__".
# So this condition: evaluates to True only if the file is being run directly (not imported as a module).
if __name__ == "__main__" :
    queue_obj = MyQueue()

    print("is_empty(): " + str(queue_obj.isEmpty()))
    print("end(): " + str(queue_obj.end()))
    print("start(): " + str(queue_obj.start()))
    print("size(): " + str(queue_obj.size()))
    print("Enqueue few elements in queue")
    for i in range(0, 10):
        queue_obj.enqueue(i)
    queue_obj.items.print_linked_list()
    print("Dequeue twice")
    for i in range(2):
        queue_obj.dequeue()
    queue_obj.items.print_linked_list()