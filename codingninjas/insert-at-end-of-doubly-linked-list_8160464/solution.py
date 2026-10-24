class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next


# Please do not change code above.


def insertAtTail(head: Node, k: int) -> Node:
    # Write your code here
 
    if head is None:
        return Node(k)

    temp = head

    while temp.next is not None:
        temp = temp.next

    new_node = Node(k)
    new_node.prev = temp
    temp.next = new_node

    return head
