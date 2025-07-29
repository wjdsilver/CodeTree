n, k = map(int, input().split())
x = []
c = []
fin=0

for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

arr = [0] * (max(x) + k) 

for pos, ch in zip(x, c):
    arr[pos] = ch

max_score = 0

for i in range(1, len(arr)-k):
    ans = 0
    for j in range(k+1):
        if arr[i + j] == "H":
            ans += 2
        elif arr[i + j] == "G":
            ans += 1
    fin = max(fin, ans)

print(fin)

