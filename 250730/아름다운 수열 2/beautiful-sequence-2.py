N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()
cnt=0

for i in range(len(A)-len(B)+1):
    com=A[i:i+len(B)]
    com.sort()
    pretty=True
    for j in range(len(B)):
        if B[j]!=com[j]:
            pretty=False
    if pretty==True:
        cnt+=1
print(cnt)