class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.data = value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Track tail for faster insertion and deletion
        
    def get_head(self):
        return self.head
    
    def get_tail(self):
        return self.tail
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    
    def insert_at_head(self, data):
        # Create a new node containing specified data
        new_node = Node(data)
        # New node points to the head, which has older data
        new_node.next = self.head
        # As this new node is now the new head, set its prev pointer to None
        new_node.prev = None
        
        if self.head is not None:
            # Given head will now have a predecessor 
            # it's important to point the previous pointer to new data
            self.head.prev = new_node
        else:
            # If list is empty tail must also point to new_node
            self.tail = new_node
        
        # Once both new node and curr head have their pointers updated
        # Set head to new node
        self.head = new_node
        
        return self.head
    
    def insert_at_tail(self, data):
        # Create a new node containing specified data
        new_node = Node(data)
        
        # Check if linkedList is empty before iterating
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            # Take advantage of self.tail, 
            # as it reduces one while loop of traversing to the end of linked list
            self.tail.next = new_node
            # One the list element in linked list is set to new node
            # Set new node's prev pointing to current node to complete doubly linked list
            new_node.prev = self.tail
            self.tail = new_node
        return self.head
    
    def insert_at_position(self, data, position):
        # Check if its a valid position
        if position < 0:
            return self.head
        
        if position == 1:
            self.insert_at_head(data)
            return self.head
        
        curr_node = self.head
        new_node = Node(data)
        
        # Iterate through position 1 to previous index of intended insertion
        for _ in range(1, position -1):
            if curr_node is not None:
                curr_node = curr_node.next
        
        # If position is out of bounds (i.e., list is too short)
        if curr_node is None:
            print("Position out of bounds")
            return self.head
        
        # Point new node's next to curr_node's next, likewise for prev pointer
        new_node.next = curr_node.next
        new_node.prev = curr_node
        
        if curr_node.next is not None:
            curr_node.next.prev = new_node
        else:
            # We're inserting at the end, so update tail
            self.tail = new_node

        
        # new node will take the place of curr_node.next
        curr_node.next = new_node
        return self.head
    
    def delete_at_head(self):
        curr_node = self.get_head()
        if curr_node is None:
        # List is already empty
            return

        if curr_node.next is None:
            # Only one node in the list
            self.head = None
            self.tail = None
        else:
            # More than one node
            self.head = curr_node.next
            self.head.prev = None
        return
    
    def delete_at_tail(self):
        curr_node = self.tail
        if curr_node is None:
            return
        
        if curr_node.prev is None:
        # Only one node
            self.head = None
            self.tail = None
        else:
            # More than one node
            self.tail = curr_node.prev
            self.tail.next = None
        return
    
    def delete_at_position(self, position):
        # Check if position is valid
        if position < 0:
            return
        
        # Check if linked list is empty
        if self.head is None:
            print("List is empty")
            return
        
        # Deleting the head
        if position == 1:
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return
        
        # Traverse to the node before the one to delete
        curr_node = self.head
        
        for _ in range(1, position - 1):
            if curr_node is not None:
                curr_node = curr_node.next
            else:
                print("Position out of bounds")
                return
            
        # If next node is None, position is out of bounds
        if curr_node is None or curr_node.next is None:
            print("Position out of bounds")
            return
        
        node_to_delete = curr_node.next
        curr_node.next = node_to_delete.next
        
        if node_to_delete.next is not None:
            node_to_delete.next.prev = curr_node
        else:
            self.tail = curr_node
        
        return
    
    def search(self, data):
        curr_node = self.head
        while curr_node is not None and curr_node.data != data:
            curr_node = curr_node.next
        return curr_node

    def print_linked_list(self):
        if self.isEmpty():
            print("List is empty")
            return False
        else:
            curr_node = self.head
            while curr_node.next is not None:
                print(curr_node.data, end=" <-> ")
                curr_node = curr_node.next
            print(curr_node.data, end=" <-> None\n")
            return True
        
    def print_reversed_list(self):
        if self.isEmpty():
            print("List is empty")
            return False
        else:
            curr_node = self.tail
            while curr_node is not None:
                print(curr_node.data, end=" <-> " if curr_node.prev else " <-> None\n")
                curr_node = curr_node.prev
            return True
        
# When a Python file is run directly, the interpreter sets a built-in variable called __name__ to "__main__".
# So this condition: evaluates to True only if the file is being run directly (not imported as a module).
if __name__ == "__main__":  
    dll = LinkedList()
    dll.print_linked_list()

    print("\nInserting values into linked list at head")
    for i in range(1,6):
        dll.insert_at_head(i)
    dll.print_linked_list()

    print("\nInserting values into linked list at tail")
    for i in range(6,11):
        dll.insert_at_tail(i)
    dll.print_linked_list()

    print("\nInserting values 11 and 6 at positions 11 and 1 respectively")
    dll.insert_at_position(11, 11)
    dll.insert_at_position(6,1)
    dll.print_linked_list()

    print("\nReversed linked list")
    dll.print_reversed_list()

    print("\nDelete element from head")
    dll.delete_at_head()
    dll.print_linked_list()

    print("\nDelete element from tail")
    dll.delete_at_tail()
    dll.print_linked_list()

    print("\nInserting values 12 at position 6")
    dll.insert_at_position(12, 6)
    dll.print_linked_list()

    print("\nSearch element 12 in linkedList")
    result = dll.search(12)
    print(f"Search result: {f'{result.data} exists' if result else 'Not found'}")

    print("\nDelete element from position 6")
    dll.delete_at_position(6)
    dll.print_linked_list()

    print("\nSearch element 12 in linkedList")
    result = dll.search(12)
    print(f"Search result: {f'{result.data} exists' if result else 'Not found'}")