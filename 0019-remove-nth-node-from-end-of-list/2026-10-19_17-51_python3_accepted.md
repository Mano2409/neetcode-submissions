# 19. Remove Nth Node From End of List
  
<br>**Problem:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/<br>

**Difficulty:** Medium<br>
**Topics:** Linked List, Two Pointers<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-10-19 17:51 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 19.2 MB (beats 63.84349999999999%)


<!-- leetgit:submissionId=2176200189 codeHash=de42761e70b49f48ca9c322a9966198196e5021d6a1a5153e268c6b325a001f1 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
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

```
