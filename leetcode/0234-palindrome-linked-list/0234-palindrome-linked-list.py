# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        array=[]
        temp=head
        while temp is not None :
            array.append(temp.val)
            temp=temp.next
        left=0
        right=len(array)-1
        while left<right:
            if array[left]!=array[right]:
                return False
            left+=1
            right-=1
        return True 
