class evaluation:

    def __init__(self):
        self.stack=[]
     

    def isEmpty(self):
        if self.stack==[]:
            return True
        return False

    def push(self,data):
        self.stack.append(data)
        
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return '$'
    
    def evaluate_postfix(self, expr):
        for i in expr:
            if i.isdigit():
                self.push(i)
            else:
                a = self.pop()
                b = self.pop()
                self.push(str(eval(b+i+a)))
        return int(self.pop())
            


e = evaluation()

exp = e.evaluate_postfix("234*6*+")
print(exp)       