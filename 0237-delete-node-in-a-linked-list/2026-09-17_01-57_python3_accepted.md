# 237. Delete Node in a Linked List
  
<br>**Problem:** https://leetcode.com/problems/delete-node-in-a-linked-list/<br>

**Difficulty:** Medium<br>
**Topics:** Linked List<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-17 01:57 local time

**Runtime:** 46 ms (beats 67.69850000000004%)
**Memory:** 19.3 MB (beats 93.06890000000001%)


<!-- leetgit:submissionId=2144100021 codeHash=b31686df16e00256e0d37d970b96ca8c49e4a6e2ab0ef43431b119e6518404ca notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next
```
