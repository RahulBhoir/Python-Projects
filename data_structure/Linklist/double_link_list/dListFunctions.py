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
