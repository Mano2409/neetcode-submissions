# 328. Odd Even Linked List
  
<br>**Problem:** https://leetcode.com/problems/odd-even-linked-list/<br>

**Difficulty:** Medium<br>
**Topics:** Linked List<br>
**Language:** python3<br>
**Status:** Accepted<br>
**Submitted:** 2026-09-19 11:39 local time

**Runtime:** 0 ms (beats 100%)
**Memory:** 21.1 MB (beats 76.6496%)


<!-- leetgit:submissionId=2146353038 codeHash=fe0f621075df2ab2db9fe6f46c2d8f2c637c5a27b6eae8bf1e8ff8368ae20fda notesHash=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 -->

## Solution

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        temp=head
        count=1
        if head == None or head.next == None:
            return head 
        
        while temp!=None:
            if count%2!=0:
                if count==1:
                    oddhead=temp
                    oddtail=temp
                else:
                    oddtail.next=temp 
                    oddtail=temp


            else:
                if count==2:
                    evenhead=temp
                    eventail=temp
                else:
                    eventail.next=temp
                    eventail=temp
            temp=temp.next
            count+=1
        eventail.next=None
        oddtail.next=evenhead
        return oddhead



        
```
