# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, curr = None, head

        while curr is not None:
            if curr.val == val:
                if curr == head:
                    head = curr.next
                    curr = head
                else:
                    prev.next = curr.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return head


        