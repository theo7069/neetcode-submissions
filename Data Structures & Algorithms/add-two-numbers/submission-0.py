# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []

        curr = l1
        while curr:
            list1.append(curr.val)
            curr = curr.next

        curr = l2
        while curr:
            list2.append(curr.val)
            curr = curr.next

        num1 = int("".join(str(x) for x in list1[::-1]))
        num2 = int("".join(str(x) for x in list2[::-1]))

        total = num1 + num2

        s = str(total)[::-1]

        dummy = ListNode()
        curr = dummy

        for ch in s:
            curr.next = ListNode(int(ch))
            curr = curr.next

        return dummy.next
        