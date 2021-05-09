# 1 -> 2 -> 3 -> 4 -> 5 -> None

# Given a Linked List and a number n,
# returns the value at the n’th node from the end of the Linked List.


LIST_IS_EMPTY = 'list is empty :('


def PrintValues(head):
    if head is None:
        return LIST_IS_EMPTY
    print('Element in LL are:')
    temp = head
    while temp != None:
        print(temp.val, end=' --> ')
        temp = temp.next
    print('NULL')
    return


# find the Nth node from last
def NthNodeFromLast(head, n):
    if head is None:
        return LIST_IS_EMPTY
    main_ptr = head
    for _ in range(n):
        head = head.next
    while head != None:
        head = head.next
        main_ptr = main_ptr.next
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
        return LIST_IS_EMPTY
    count_of_number = 0
    while head != None:
        if head.val == number:
            count_of_number += 1
        head = head.next
    return count_of_number


# remove duplicates from sorted linked list
def RemoveDuplicates(head):
    if head is None:
        return LIST_IS_EMPTY
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
        return LIST_IS_EMPTY
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
        return LIST_IS_EMPTY
    hash_set = set()
    while head.next is not None:
        if head in hash_set:
            return True
        hash_set.add(head)
        head = head.next
    return False


# reverse a single link list
def ReverseList(head):
    if head is None:
        return LIST_IS_EMPTY
    prev_ptr = None
    curr_ptr = head
    while curr_ptr != None:
        next_ptr = curr_ptr.next
        curr_ptr.next = prev_ptr
        prev_ptr = curr_ptr
        curr_ptr = next_ptr
    return prev_ptr


# bring last element to front
def LastElementToFirst(head):
    if head is None:
        return LIST_IS_EMPTY
    temp = head
    # while temp.next != None:
    #     if temp.next.next == None:
    #         last_node = temp.next
    #         temp.next = None
    #         last_node.next = head
    #         head = last_node
    #         return head
    #     temp = temp.next

    while temp.next.next != None:
        temp = temp.next
    temp.next.next = head
    head = temp.next
    temp.next = None
    return head


# swapping node values
def SwapData(head, data1, data2):
    temp = head
    while temp is not None:
        if temp.data == data1:
            temp.data = data2
        elif temp.data == data2:
            temp.data = data1
        temp = temp.next
