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
        
       
        