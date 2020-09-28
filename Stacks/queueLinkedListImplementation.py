import sys
class Node:

    def __init__(self, info):
        self.info = info
        self.next = None


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        if self.front == None:
            return True
        return False

    def enqueue(self, info):
        temp = Node(info)
        if temp is None:
            print("No Memory")
            return
        if self.isEmpty():
            self.front = temp
            self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow ")
            sys.exit(0)
        d = self.front.info
        self.front = self.front.next
        return d
        
    def display(self):
        if self.isEmpty():
            print("Queue Underflow")
            sys.exit(0)
        else:
            temp = self.front
            while temp != None:
                print(temp.info)
                temp = temp.next
            
if __name__ == "__main__":
    
    q = Queue()
    while(1):
        print("1. Push")
        print("2. Pop")
        print("3. Display all elements")
        print("4. Quit")
        print("Enter your choice: ")
        choice = int(input())
        if choice == 1:
            value = int(input("Enter a value to insert:"))
            q.enqueue(value)
        elif choice == 2:
            d = q.dequeue()
            print("Popped element ",d)
        elif choice == 3:
            q.display()
        else:
            sys.exit(0)
