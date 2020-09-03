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

    def rev_expr(self, expr):
        revexpr = ''
        for c in expr:
            revexpr = c + revexpr
        return revexpr
    
    def evaluate_Prefix(self, expr):
        exp = self.rev_expr(expr)
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                a = self.pop()
                b = self.pop()
                self.push(str(eval(b+i+a)))
        return int(self.pop())
            


e = evaluation()

exp = e.evaluate_Prefix("*+234")
print(exp)       