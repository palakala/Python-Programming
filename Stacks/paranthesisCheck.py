def check(exp):
    
    s=[]

    for i in range(len(exp)):
        if exp[i]=='(' or exp[i]=='[' or exp[i]=='{':
            s.append(exp[i])
            continue
        # checking if the exp is starting with closing brackets or not
        if len(s)==0:
            return False

        if exp[i]==')':
            x=s.pop()
            
            if x=='[' or x=='{':
                return False

        if exp[i]==']':
            x=s.pop()
            if x=='(' or x=='{':
                return False
        if exp[i]=='}':
            x=s.pop()
            if x=='[' or x=='(':
                return False
    # Checking if any paranthesis is left or not
    if len(s):
        return False
    else:
        return True
if __name__ == "__main__":

    exp=input("Enter Expression")

    if check(exp):
        print("Balanced")
    else:
        print("Not Balanced")

        
