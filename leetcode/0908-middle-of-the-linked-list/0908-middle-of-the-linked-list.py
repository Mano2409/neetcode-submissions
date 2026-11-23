# Definition for singly-linked list.
# class ListNode:
#     def __init__(sef, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        
        length=0
        temp=head
        while temp is not None :
            length+=1
            temp=temp.next 
        middle=length//2
        temp=head
        
        for i in range(middle):
            temp=temp.next
        return temp