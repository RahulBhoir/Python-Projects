# 1 -> 2 -> 3 -> 4 -> 5 -> None

# Given a Linked List and a number n,
# returns the value at the n’th node from the end of the Linked List.
def NthNodeFromLast(head, n):
    if head is None:
        return 'list is empty'
    main_ptr = head
    for _ in range(n):
        head = head.next
        value = head.val
    while head != None:
        head = head.next
        main_ptr = main_ptr.next
        main = main_ptr.val
    return main_ptr.val


# Given a singly linked list, find the middle of the linked list.
def MiddleNode(head):
    faster_ptr = head
    slower_ptr = head
    while faster_ptr != None and faster_ptr.next != None:
        faster_ptr = faster_ptr.next.next
        slower_ptr = slower_ptr.next
    return slower_ptr.val


# count number of occurrences of given key in linked list.
def CountTheElement(head, number):
    if head is None:
        return 'the list is empty'
    count_of_number = 0
    while head != None:
        if head.val is number:
            count_of_number += 1
        head = head.next
    return count_of_number


def RemoveDuplicates(head):
    if head is None:
        return 'the list is empty'
    while head.next != None:
        print(head.next.val)
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return
