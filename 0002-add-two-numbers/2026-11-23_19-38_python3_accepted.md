# 2. Add Two Numbers
  
<br>**Problem:** https://leetcode.com/problems/add-two-numbers/<br>

**Difficulty:** Medium<br>
**Topics:** Linked List, Math, Recursion<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-11-23 19:38 local time

**Runtime:** 5 ms (beats 43.1582%)
**Memory:** 19.3 MB (beats 56.239599999999996%)


<!-- leetgit:submissionId=2201961892 codeHash=98e993b2d12350a8f6681f9cf83e7bc298fcb593dd88c7bfc3760fb9fbc06833 notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        number1=0
        place1=1
        temp1=l1
        while temp1 is not None:
            number1+=temp1.val*place1
            place1*=10
            temp1=temp1.next
        number2=0
        place2=1
        temp2=l2
        while temp2 is not None:
            number2+=temp2.val*place2
            place2*=10
            temp2=temp2.next
        total=number1+number2
        if total==0:
            return ListNode(total)
        head=None
        curr=None
        while total>0:
            new=ListNode(total%10)
            if head is None :
                head=new
                curr=new
            else:
                curr.next=new
                curr=new
            total//=10
        return  head 
        
       
        
```
