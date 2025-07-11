MAX_T = 200000
A_path = [-1] * (MAX_T + 1)
B_path = [-1] * (MAX_T + 1)

def simulate(commands, path):
    cur = 1000
    t = 0
    for d, sec in commands:
        sec = int(sec)
        for _ in range(sec):
            t += 1
            if d == 'L':
                cur -= 1
            else:
                cur += 1
            path[t] = cur


n, m = map(int, input().split())
A_cmd = [input().split() for _ in range(n)]
B_cmd = [input().split() for _ in range(m)]


simulate(A_cmd, A_path)
simulate(B_cmd, B_path)


for t in range(1, MAX_T + 1):
    if A_path[t] != -1 and A_path[t] == B_path[t]:
        print(t)
        break
else:
    print(-1)
