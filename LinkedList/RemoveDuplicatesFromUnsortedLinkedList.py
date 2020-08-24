# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Tc : O(n); SC : O(n) this approach works with unsorted list
        hash_set = set()
        res = temp = ListNode(0)
        curr = head
        while curr:
            print(curr.val)
            if curr.val not in hash_set:
                hash_set.add(curr.val)
                temp.next = ListNode(curr.val)
                temp = temp.next
            curr = curr.next
        return res.next

        # Approach for sorted linked list
        # TC : O(n); SC : O(1)
        # if head is None:
        #     return head
        # curr = head
        # while curr and curr.next:
        #     if curr.val == curr.next.val:
        #         curr.next = curr.next.next
        #     else:
        #         curr = curr.next
        # return head