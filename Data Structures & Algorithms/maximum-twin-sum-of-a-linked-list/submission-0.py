# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        nodes = []
        res = 0
        while curr:
            nodes.append(curr)
            curr = curr.next
        l , r = 0, len(nodes) - 1
        while l < r:
            res = max(res, nodes[l].val + nodes[r].val)
            l += 1
            r -= 1
        return res
        