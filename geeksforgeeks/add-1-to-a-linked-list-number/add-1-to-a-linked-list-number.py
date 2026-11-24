''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def reverse(self,head):
        temp=head
        prev=None
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev
        
    def addOne(self,head):
        # code here
        head=self.reverse(head)
        carry=1
        temp=head
        last=None
        while temp is not None:
            total=temp.data+carry
            temp.data=total%10
            carry=total//10
            if carry==0:
                break
            last=temp
            temp=temp.next
        if  carry==1:
            last.next=Node(1)
        return self.reverse(head)
        