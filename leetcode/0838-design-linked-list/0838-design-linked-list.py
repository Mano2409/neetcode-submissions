class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        count = 0

        while temp != None:
            if count == index:
                return temp.val
            temp = temp.next
            count += 1

        return -1

    def addAtHead(self, val: int) -> None:
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)

        if self.head == None:
            self.head = newnode
            return

        temp = self.head

        while temp.next != None:
            temp = temp.next

        temp.next = newnode

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        temp = self.head
        count = 0

        while temp != None:
            if count == index - 1:
                newnode = Node(val)
                newnode.next = temp.next
                temp.next = newnode
                return

            temp = temp.next
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        count = 0

        while temp.next != None:
            if count == index - 1:
                temp.next = temp.next.next
                return

            temp = temp.next
            count += 1