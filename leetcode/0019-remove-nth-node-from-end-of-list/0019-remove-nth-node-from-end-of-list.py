class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head is None:
            return None

        res = ListNode(0, head)
        fast = head
        slow = res

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return res.next
