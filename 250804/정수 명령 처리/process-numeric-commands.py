N = int(input())


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


s = Stack()


for _ in range(N):
    line = input().split()
    cmd=(line[0])
    if cmd== "push":
        s.push(int(line[1]))
    elif cmd == "pop":
        print(s.pop())
    elif cmd == "size":
        print(s.size())
    elif cmd== "empty":
        print(1 if s.empty() else 0)
    elif cmd== "top":
        print(s.top())