# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        result = 0

        a = ""
        b = ""
        while l1:
            a += str(l1.val)
            l1 = l1.next

        while l2:
            b += str(l2.val)
            l2 = l2.next

        result = int(a[::-1]) + int(b[::-1])

        dummy_head = ListNode()
        current = dummy_head

        for digit in str(result)[::-1]:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy_head.next
