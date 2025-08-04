str = input()

class Stack:
    def __init__(self):
        self.items = []
                
    def push(self, item):
        self.items.append(item)
                
    def empty(self):
        return not self.items
                
    def size(self):
        return len(self.items)
        
    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
            
        return self.items.pop()
                
    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
                        
        return self.items[-1]


def solution(x):
    s = Stack()
    for i in range(len(x)):
        if x[i] == '(' :
            s.push('(')
            
        else:
            if s.empty() == True:
                return False
            s.pop()

    if s.empty() == False:
        return False
    return True

print("Yes" if solution(str) else "No")