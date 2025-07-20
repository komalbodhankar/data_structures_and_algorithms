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
                # Deleting the head
                llist.head = curr_node.next
                curr_node = llist.head # reset curr_node to head, as we now have new head
            else:
                # Map previous's next with current's next
                prev_node.next = curr_node.next
                curr_node = curr_node.next # set pointer to next node
        else:
            prev_node = curr_node # After each iteration, update prev node
            curr_node = curr_node.next # Iterate to next node
    return llist.head # Return the resulting linked list
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

print("\nAdding new elements to it")
for i in range(4):
    llist.insert_at_head(7)
llist.print_linked_list()

print("\nDelete all occurances of 7 from linked list")
delete_all_occurances(llist, 7)
llist.print_linked_list()

