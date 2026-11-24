# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        dummy=ListNode(0,head)
        slow=dummy
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        temp=slow.next
        prev=None
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front 
        p1=head
        p2=prev
        while p2 is not None:
            if p1.val!=p2.val:
                return False
            p1=p1.next
            p2=p2.next
        return True 
            
        
        