# 160. Intersection of Two Linked Lists
  
<br>**Problem:** https://leetcode.com/problems/intersection-of-two-linked-lists/<br>

**Difficulty:** Easy<br>
**Topics:** Hash Table, Linked List, Two Pointers<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-20 18:34 local time

**Runtime:** 127 ms (beats 6.124900000000011%)
**Memory:** 38 MB (beats 77.57720000000003%)


<!-- leetgit:submissionId=2147695595 codeHash=d27278a9eb2720b69f03792aea14af4b74d91a602509a65e2c306e660e140fac notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA
        b=headB
        lengthA=0
        lengthB=0
        while a!=None:
            a=a.next
            lengthA+=1
        while b!=None:
            b=b.next
            lengthB+=1
        a=headA
        b=headB
        while lengthA>lengthB:
            a=a.next

            lengthA-=1
        
        while lengthB>lengthA:
            b=b.next
            lengthB-=1
        while a!=b:
            a=a.next
            b=b.next
        return a
        
        
```
