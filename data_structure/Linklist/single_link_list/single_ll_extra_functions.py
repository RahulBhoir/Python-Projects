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


# check if the linked list has loop or not
# Floyd’s Cycle-Finding Algorithm
def CheckLoop(head):
    if head is None:
        return 'the list is empty'
    slow_ptr = head
    fast_ptr = head
    while slow_ptr and fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            return True
    return False


def CheckLoop_v2(head):
    if head is None:
        return 'the list is empty'
    hash_set = set()
    while head.next is not None:
        if head in hash_set:
            return True
        hash_set.add(head)
        head = head.next
    return False


def ReverseList(head):
    if head is None:
        return 'the list is empty'
    prev_ptr = None
    curr_ptr = head
    while curr_ptr != None:
        next_ptr = curr_ptr.next
        curr_ptr.next = prev_ptr
        prev_ptr = curr_ptr
        curr_ptr = next_ptr
    return prev_ptr
