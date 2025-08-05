
from collections import deque

dq = deque()        # 정수를 관리할 deque를 선언합니다. => 빈 덱

n = int(input())

for _ in range(n):
    line = input().split()
    if line[0] =="push_front":
        dq.appendleft(int(line[1]))
    elif line[0]=="push_back":
        dq.append(int(line[1]))
    elif line[0]=="pop_front":
        print(dq.popleft())
    elif line[0]=="pop_back":
        print(dq.pop())
    elif line[0]=="size":
        print(len(dq))
    elif line[0]=="empty":
        print(0 if dq else 1)
    elif line[0]=="front":
        print(dq[0])
    elif line[0]=="back":
        print(dq[-1])

