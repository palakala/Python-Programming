import sys
class stack:
    def __init__(self):
        self.stack =[None]*100
        self.top=-1

    def isFull(self):
        if self.top==100:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top==-1:
            return True
        return False
    
    def push(self,ele):
        if self.isFull():
            print("stack overflow")
            return
        self.top+=1
        self.stack[self.top]= ele
    
    def pop(self):
        if self.isEmpty():
            print("Stack Uderflow")
            return
        d = self.stack[self.top]
        self.top-=1
        return d

    def peek(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        d= self.stack[self.top]
        return d
    
    def display(self):
        if self.isEmpty():
            print("Stack is empty")
            sys.exit(0)
        temp=self.top
        while temp>=0:
            print(self.stack[temp])
            temp-=1

if __name__=='__main__':

    s= stack()
    while(1):
        print("1.Push")
        print("2.Pop")
        print("3.Peek")
        print("4.Display all stack elements")
        print("5. Exit")
        print("Enter your choice")
        choice = int(input())
        if choice==1:
            value=int(input("Enter value to push"))
            s.push(value)
        elif choice==2:
            d=s.pop()
            print("popped element ",d)
        elif choice==3:
            print("Top of the stack is ", s.peek)
        elif choice==4:
            s.display()
        else:
            sys.exit(0)
