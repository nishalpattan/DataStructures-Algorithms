class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number = self.toInteger(l1) + self.toInteger(l2)
        return number

    def toInteger(self, l1:ListNode) -> int:
        number = 0
        increment = 1
        while l1.next:
            number = number + (l1.value * increment)
            increment = increment * 10
            l1= l1.next
        return number

if __name__ == "__main__" :
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l2 = ListNode(3)
    l2.next = ListNode(4)
    s = Solution()
    print(s.toInteger(l1))

