n, m = tuple(map(int, input().split()))

a_arr = [
    tuple(input().split())
    for _ in range(n)
]

b_arr = [
    tuple(input().split())
    for _ in range(m)
]

a_ans = []
a_start_idx = 0

for d, t in a_arr:
    t = int(t)
    if d == 'R':
        while t > 0:
            a_start_idx += 1
            t-= 1
            a_ans.append(a_start_idx)
    
    else:
        while t > 0:
            a_start_idx -= 1
            t -= 1
            a_ans.append(a_start_idx)

b_ans = []
b_start_idx = 0

for d, t in b_arr:
    t = int(t)
    if d == 'R':
        while t > 0:
            b_start_idx += 1
            t -= 1
            b_ans.append(b_start_idx)
    
    else:
        while t > 0:
            b_start_idx -= 1
            t -= 1
            b_ans.append(b_start_idx)

ans = 0
for i in range(max(len(a_ans), len(b_ans))):
    if a_ans[i] == b_ans[i]:
        ans = i+1
        print(ans)
        break
    if i == max(len(a_ans), len(b_ans)) - 1:
        print(-1)

