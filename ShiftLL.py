# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def shiftLinkedList(head, k):
    list_len = 1
    list_tail = head
    while list_tail.next:
        list_tail = list_tail.next
        list_len += 1
    k = k % list_len
    new_tail_pos = list_len - k
    new_tail = head
    for i in range(1,new_tail_pos):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    list_tail.next = head


if __name__ == "__main__":
    node = LinkedList(0)
    node.next = LinkedList(1)
    node.next.next = LinkedList(2)
    node.next.next.next = LinkedList(3)
    node.next.next.next.next = LinkedList(4)
    node.next.next.next.next.next = LinkedList(5)
    shiftLinkedList(node, 2)



