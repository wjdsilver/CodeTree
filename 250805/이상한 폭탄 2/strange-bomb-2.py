N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]
fin = 0

for i in range(N):
    for j in range(i + 1, min(N, i + K + 1)):
        if num[i] == num[j]:
            fin = max(fin, num[i])
            break
print(fin)