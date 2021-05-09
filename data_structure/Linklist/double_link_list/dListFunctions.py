LIST_IS_EMPTY = 'list is empty :('


def PrintValues(head):
    if head is None:
        return LIST_IS_EMPTY
    print('Element in LL are:')
    temp = head
    while temp != None:
        print(temp.val, end=' ')
        temp = temp.next
    print()
    return


def ReverseList(head):
    if head is None:
        return LIST_IS_EMPTY
    temp = head
    while temp != None:
        next_node = temp.next
        prev_node = temp.prev
        temp.next = prev_node
        temp.prev = next_node
        if next_node is None:
            head = temp
            return head
        temp = next_node
    return head
