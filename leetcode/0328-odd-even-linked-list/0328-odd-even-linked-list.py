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



        