# 160. Intersection of Two Linked Lists
  
<br>**Problem:** https://leetcode.com/problems/intersection-of-two-linked-lists/<br>

**Difficulty:** Easy<br>
**Topics:** Hash Table, Linked List, Two Pointers<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-11-25 15:58 local time

**Runtime:** 117 ms (beats 45.95000000000001%)
**Memory:** 38.3 MB (beats 14.568199999999997%)


<!-- leetgit:submissionId=2203159197 codeHash=321be92dd125dbb2e719888a088725427bbd9fcc4d6cd20f5532e338362ed7fc notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        arr=set()
        temp=headA
        while temp is not None:
            arr.add(temp)
            temp=temp.next
        temp=headB
        while temp is not None:
            if temp in arr:
                return temp
            temp=temp.next
        return None 
```
