# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None 
        odddummy=ListNode(0)
        oddcurr=odddummy
        temp=head
        while temp is not None:
            oddcurr.next=ListNode(temp.val)
            oddcurr=oddcurr.next
            if temp.next is None :
                break
            temp=temp.next.next
        evendummy=ListNode(0)
        evencurr=evendummy
        temp=head.next
        while temp is not None:
            evencurr.next=ListNode(temp.val)
            evencurr=evencurr.next
            if temp.next is None:
                break
            temp=temp.next.next
        oddcurr.next=evendummy.next
        return odddummy.next
