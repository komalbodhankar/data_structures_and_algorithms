import sys
import os
sys.path.append(os.path.abspath('..'))

from data_structures.singly_linked_list import LinkedList

def delete_all_occurances(llist: LinkedList, value):
    curr_node = llist.head
    prev_node = None
    
    while curr_node is not None:
        if curr_node.data == value:
            if prev_node is None:
                llist.head = curr_node.next
            else:
                prev_node.next = curr_node.next
        prev_node = curr_node
        curr_node = curr_node.next
    return llist.head
print("\n___________________________________")
print("\nCreating a new blank linked list")
llist = LinkedList()
llist.print_linked_list()

print("\nAdding new elements to it")
for i in range(1,11):
    if i % 2 == 0:
        llist.insert_at_head(2)
    else:
        llist.insert_at_head(1)
llist.print_linked_list()

print("\nDelete all occurances of 2 from linked list")
delete_all_occurances(llist, 2)
llist.print_linked_list()
