#
#
#
from LinkedList import LinkedList

# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    print('Empty List:')
    llist.printList()

    # Insert 6.  So linked list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7);

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1);

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)

    # Insert 88, 77, 99 at the beginning. So linked list becomes 88-> 77-> 99-> 1-> 7-> 8-> 6-> 4-> None
    llist.push(99);
    llist.push(77);
    llist.push(88);

    print('Created linked list is:')
    llist.printList()

    llist.deleteNode(1)
    print("\nLinked List after Deletion of 1:")
    llist.printList()

    llist.deleteNodeAt(4)
    print("\nLinked List after Deletion of node at position 4:")
    llist.printList()

    keyFind = 21
    if llist.iterativeSearch(keyFind):
        print("Yes")
    else:
        print("No")

    keyFind = 6
    if llist.recursiveSearch(llist.head, keyFind):
        print("Yes")
    else:
        print("No")

