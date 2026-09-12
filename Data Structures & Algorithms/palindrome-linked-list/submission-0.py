# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        nodes = []
        while curr != None:
            nodes.append(curr)
            curr = curr.next
        l,r = 0, len(nodes) - 1
        while l < r:
            if(nodes[l].val != nodes[r].val):
                return False
            l += 1
            r -= 1
        return True

        