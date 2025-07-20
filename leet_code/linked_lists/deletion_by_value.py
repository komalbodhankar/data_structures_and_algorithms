'''
Given the head of a singly linked list and a value to be deleted from the linked list, 
if the value exists in the linked list, delete the value and return TRUE. 
Otherwise, return FALSE.

Constraints:
Let n be the number of nodes in the linked list:
    1 ≤ n ≤ 500
    -5000 ≤ Node.data ≤ 5000
'''

import sys
import os
sys.path.append(os.path.abspath('..'))

from data_structures.singly_linked_list import LinkedList as SinglyLinkedList
def deletion_by_value(llist: SinglyLinkedList, value):
    deleted = False
    curr_node = llist.head
    prev_node = None
    
    while curr_node:
        if curr_node.data == value:
            if prev_node is None:
                # Deletion at head
                llist.head = curr_node.next
                curr_node = llist.head
            else:
                # Skip next node
                prev_node.next = curr_node.next
                curr_node = curr_node.next
                deleted = True
                break
        else:        
            prev_node = curr_node
            curr_node = curr_node.next
    return deleted

llist = SinglyLinkedList()

print("\nInsert few values in linkedList")
for i in range(1,11):
    llist.insert_at_tail(i)
llist.print_linked_list()

value = "Yes" if deletion_by_value(llist, 7) else "No"
print(f"\nDoes 7 exist?: {value}")

print("\nPrint resulting linked list")
llist.print_linked_list()

value = "Yes" if deletion_by_value(llist, 11) else "No"
print(f"\nDelete if 11 exists: {value}")

print("\nPrint resulting linked list")
llist.print_linked_list()
