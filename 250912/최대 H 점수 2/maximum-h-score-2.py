N, L = map(int, input().split())
a = list(map(int, input().split()))
h=0

for i in range(min(min(a),N),N+1):
    cnt=0
    hNum=0
    for j in (a):
        if j==i-1:
            cnt+=1
        if j>=i:
            hNum+=1

    if hNum+cnt>i or (hNum+cnt==i and cnt<=L):
        h=i
print(h)