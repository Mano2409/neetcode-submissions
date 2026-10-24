class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def constructDLL(arr: [int]) -> Node:
    # Write your code here
    head=Node(arr[0])
    prev=head
    for i in range(1,len(arr)):
        temp=Node(arr[i])
        prev.next=temp
        temp.prev=prev
        prev=temp
    return head
