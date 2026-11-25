# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        arr=set()
        temp=headA
        while temp is not None:
            arr.add(temp)
            temp=temp.next
        temp=headB
        while temp is not None:
            if temp in arr:
                return temp
            temp=temp.next
        return None 