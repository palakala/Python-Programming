class Node:

    def __init__(self,info,link=None):
        self.info=info
        self.link=link

class LinkedList:

    def __init__(self):
        self.head=None
    
    def insertAtBegin(self,info):
        newNode = Node(info)
        if self.head== None :
            self.head= newNode
        else:
            newNode.link= self.head
            self.head= newNode
    
    def insertAtEnd(self,info):
        newNode = Node(info)
        if self.head != None:
            current = self.head
            while current.link != None:
                current= current.link
            current.link=newNode
        else:
            self.head=newNode
    
    def deleteNode(self, element):

        if self.head== None:
            print("List is empty")
            return
        elif self.head.link == element:
            temp = self.head
            self.head = temp.link
            temp = None
            return
        else:
            current = self.head
            while current.link != None:
                if current.link.info == element:
                    temp = current.link
                    current.link = temp.link
                    temp = None
                    return
                current = current.link
            print("Element is not found to delete")

    
    def display(self):
        if self.head != None:
            current = self.head
            while current != None:
                print(current.info)
                current = current.link
        else:
            print("List is empty")
        
    def search(self, search):
        current = self.head
        if current == None:
            print("List is empty Nothing to search")
            return
        while current != None:
            if current.info == search:
                print("Element", search ,"found")
                return
            current = current.link
        print("Element " + str(search) + " not found")



LL = LinkedList()
LL.insertAtBegin(20)
LL.insertAtBegin(50)
LL.display()
print("************* ")
LL.insertAtEnd(30)
LL.insertAtEnd(90)
LL.display()
print("After deleting")
LL.deleteNode(20)
LL.display()
LL.search(40)
LL.search(90)

