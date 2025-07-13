'''
Unlike Java, Python does not have a built-in function for linkedLists
Here we will be implementing a singly-linked-list from scratch
'''

# A linkedList is a collection of Node classes, 
# each node has a data field to store data & next field stores location where next data resides
class Node:
    def __init__(self, data):
        self.data = data # Data or val field
        self.next = None # Pointer to next node

class LinkedList:
    def __init__(self):
        self.head = None # Pointer to the first node
    
    def get_head(self):
        return self.head
    
    def isEmpty(self):
        if self.head is None: # Check whether the head is None
            return True
        else:
            return False
    
    def insert_at_head(self, data): # Time complexity for insertion at head = O(1)
        # Create a new node containing specified data
        new_node = Node(data)
        
        # New node points to the head, which has older data
        new_node.next = self.head
        
        # Head points to the new node
        self.head = new_node
        
        return self.head
    
    def insert_at_tail(self, data):
        # Create a new node containing specified data
        new_node = Node(data)
        
        # Check if linkedList is empty
        if (self.isEmpty()):
            self.head = new_node # Yes? point new_node to head
        else:
            curr_node = self.head # No? Traverse to the end of the linkedList and insert the new_node
        
            while curr_node.next is not None:
                curr_node = curr_node.next
            
            curr_node.next = new_node    
        return self.head
    
    def insert_at_position(self, data, position):
        # Check if position is valid
        if position < 0:
            return self.head
        
        # If position is 1 it is same as insertion at head
        if position == 1:
            self.insert_at_head(data)
            return self.head
        
        # Point curr_node to head and initialize a new node with specified data
        curr_node = self.head
        new_node = Node(data)
        
        # Iterate through position 1 to previous index of intended insertion
        for _ in range(1, position - 1):
            if curr_node is not None:
                curr_node = curr_node.next
        
        # Point new node's next to curr_node's next
        new_node.next = curr_node.next
        
        # new node will take the place of curr_node.next
        curr_node.next = new_node
        return self.head
    
    def search(self, data):
        curr_node = self.head
        while curr_node is not None and curr_node.data != data:
            curr_node = curr_node.next
        return curr_node
    
    def delete_at_head(self):
        first_element = self.get_head()
        if first_element is not None:
            self.head = first_element.next
        return
    
    def delete_at_tail(self):
        curr_node = self.get_head()
        
        # Check if list is empty
        if curr_node is None:
            return
        
        # Check if linkedList has only one element
        if curr_node.next is None:
            llist.head = None
            return 

        # Iterate until the second-last element in the linkedList
        while curr_node.next.next is not None:
            curr_node = curr_node.next
        
        # Set the last element position to None, for deleting the last node
        curr_node.next = None
        return
    
    def delete_at_position(self, position):
        # Check if position is valid
        if position < 1:
            return
        
        # Check if linkedList is empty
        if self.head is None:
            print("List is empty")
            return

        # Deleting the head
        if position == 1:
            self.head = self.head.next
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

        # Delete the node by skipping it
        curr_node.next = curr_node.next.next    
        
    def print_linked_list(self):
        if (self.isEmpty()):
            print("List is empty")
            return False
        else:
            temp_node = self.head
            while temp_node.next is not None:
                print(temp_node.data, end=" -> ")
                temp_node = temp_node.next
            print(temp_node.data, end=" -> None")
            return True
    
    def reverse(self):
        if (self.isEmpty()):
            print("List is empty")
            return False
        else:
            # Initialize 3 pts prev, next and curr. Prev and next will be None.
            prev_node = None
            curr_node = self.head
            next_node = None
            
            # As we want to traverse through each and every element in the linked list
            # We cannot use curr_node.next is not None condition, as it will skip the last element
            while curr_node is not None:
                # Point next node to curr's next
                next_node = curr_node.next
                # Point curr's next to prev node
                # **** This reverses the link ****
                curr_node.next = prev_node
                
                # Point prev to curr and curr to next to iterate through the linked list
                prev_node = curr_node
                curr_node = next_node
            
            # After all nodes are traversed, point head to prev_node.
            self.head = prev_node

llist = LinkedList()
llist.print_linked_list()

print("Inserting values into linked list at tail")
for i in range(1,10):
    llist.insert_at_tail(i)
llist.print_linked_list()

print("\nInserting 2 in the middle")
llist.insert_at_position(2, 7)
llist.print_linked_list()

print("\nInserting values into linked list at head")
for i in range(1,10):
    llist.insert_at_head(i)
llist.print_linked_list()

print("\nDelete tail element")
llist.delete_at_tail()
llist.print_linked_list()

print("\nDelete element at position 1")
llist.delete_at_position(1)
llist.print_linked_list()

print("\nDelete element at position 16")
llist.delete_at_position(16)
llist.print_linked_list()

print("\nSearch element 11 in linkedList")
result = llist.search(11)
print(f"Search result: {result.data if result else 'Not found'}")

print("\nReverse the linked list and print")
llist.reverse()
llist.print_linked_list()

                