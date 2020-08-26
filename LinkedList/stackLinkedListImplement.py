import sys
class Node:
    def __init__(self, info):
        self.info=info
        self.next=None

class stack:
    def __init__(self):
        self.top=None

    def isEmpty(self):
        if self.top is None:
            return True
        return False
    
    def push(self,info):
        temp=Node(info)
        if temp is None:
            print("Stack Overflow")
            return            
        temp.next=self.top
        self.top=temp

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return
        d= self.top.info
        self.top=self.top.next
        return d

    def peek(self):
        if self.isEmpty():
            print("Stack underflow")
            return
        d= self.top.info
        return d

    def display(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        temp=self.top
        while temp != None:
            print(temp.info)
            temp=temp.next

if __name__ == '__main__':

    s=stack()

    while(1):
        print("1. Push")
        print("2. Pop")
        print("3. Display peek")
        print("4. Display all elements")
        choice=int(input("Enter your choice"))
        if choice==1:
            value=int(input("Enter ele to push\t"))
            s.push(value)
        elif choice==2:
            s.pop()
        elif choice==3:
            s.peek()
        elif choice==4:
            s.display()
        else:
            sys.exit(0)