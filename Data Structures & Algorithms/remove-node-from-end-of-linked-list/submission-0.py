# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes1 = []
        curr = head
        while curr:
            nodes1.append(curr)
            curr = curr.next
        nodes2 = []
        for i in range(len(nodes1)):
            if i == len(nodes1) - n:
                continue
            nodes2.append(nodes1[i])
        for i in range(1, len(nodes2)):
            nodes2[i-1].next = nodes2[i]
        if not nodes2:
            return None
        nodes2[-1].next = None
        return nodes2[0]
        
        