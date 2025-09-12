N, L = map(int, input().split())
a = list(map(int, input().split()))
h=0

for i in range(min(min(a),N),N+1):#i는 H점수 후보
    cnt=0 #H-1인거(값을 1 올려 H가 될수 있는거)
    hNum=0 #숫자가 H이상인거
    for j in (a):
        if j==i-1:
            cnt+=1
        if j>=i:
            hNum+=1

    if cnt<=L:
        if  hNum+cnt>=i:
            h=i
    if cnt>L:
        if hNum+L>=i:
            h=i
print(h)