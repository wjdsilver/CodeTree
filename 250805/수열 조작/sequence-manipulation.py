from collections import deque
dq = deque()

n = int(input())

def circle(N):
    for i in range(1,N+1):
        dq.append(i)
    while len(dq) != 1:
        dq.popleft()
        dq.append(dq.popleft())
    print(dq[0])

circle(n)