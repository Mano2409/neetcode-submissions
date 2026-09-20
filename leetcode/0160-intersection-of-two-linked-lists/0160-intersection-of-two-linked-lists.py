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
        
        