class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        l, r = 0, len(nodes) - 1
        order = []

        while l <= r:
            if l == r:
                order.append(nodes[l])
            else:
                order.append(nodes[l])
                order.append(nodes[r])
            l += 1
            r -= 1

        for i in range(1, len(order)):
            order[i - 1].next = order[i]

        order[-1].next = None


        