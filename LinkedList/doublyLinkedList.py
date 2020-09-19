class Node:

    def __init__(self, info, prev= None, next= None):
        self.info = info
        self.prev = prev
        self.next = next
    
class LinkedList:

    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, info):

        newNode = Node(info)
        if self.head == None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

    def insertatEnd(self, info):
        pass

    def deleteNode(self, ele):
        pass
    


    def display(self):

        if self.head == None:
            print("List is Empty")
            return
        current = self.head
        while(current != None):
            print(current.info)
            current = current.next



LL = LinkedList()
LL.insertAtBegin(20)
LL.insertAtBegin(40)
LL.display()
    
