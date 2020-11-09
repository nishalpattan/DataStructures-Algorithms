class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


def add_linked_lists(l1,l2):
    if l1 is None or l2 is None:
        return None
    stack1 = list()
    stack2 = list()
    stack3 = list()
    temp = l3 = ListNode(0)
    carry = 0
    while l1:
        stack1.append(l1.value)
        l1 = l1.next
    while l2:
        stack2.append(l2.value)
        l2 = l2.next
    while stack1 or stack2:
        if stack1 and stack2:
            curr_sum = stack1.pop() + stack2.pop() + carry
        elif stack1:
            curr_sum = stack1.pop() + carry
        elif stack2:
            curr_sum = stack2.pop() + carry
        carry = curr_sum // 10
        stack3.append(curr_sum % 10)
    while stack3:
        temp.next = ListNode(stack3.pop())
        temp = temp.next
    return l3.next






if __name__ == "__main__":
    l1=ListNode(1)
    l1.next = ListNode(2)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    result = add_linked_lists(l1, l2)
    while result:
        print(result.value)
        result = result.next
