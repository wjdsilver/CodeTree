n, m = map(int, input().split())
arr_a=[]
arr_b=[]

p=0
for _ in range(n):
    v, t = map(int, input().split())
    for i in range(t):
            p += v
            arr_a.append(p)

p=0
for _ in range(m):
    v, t = map(int, input().split())
    for i in range(t):
            p += v
            arr_b.append(p)
        

T = min(len(arr_a), len(arr_b))

change = 0
prev = 0

for i in range(T):
    if arr_a[i] > arr_b[i]:
        curr= 1
    elif arr_a[i] < arr_b[i]:
        curr= 2
    else:
        curr= 0

    if curr != prev:
        change += 1
        prev = curr

print(change)