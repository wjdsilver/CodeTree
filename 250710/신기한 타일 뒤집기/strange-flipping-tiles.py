MAX_K = 100000
n = int(input())
a = [0] * (2 * MAX_K + 1)
b, w= 0, 0

cur = MAX_K
for _ in range(n):
    x, c = tuple(input().split())
    x = int(x)

    if c == 'L':
        while x > 0:
            a[cur] = 1
            x -= 1

            if x: 
                cur -= 1
    else:
        while x > 0:
            a[cur] = 2
            x -= 1

            if x: 
                cur += 1

for i in range(2 * MAX_K + 1):
    if a[i] == 1: 
        w += 1
    elif a[i] == 2: 
        b += 1

print(w, b)
