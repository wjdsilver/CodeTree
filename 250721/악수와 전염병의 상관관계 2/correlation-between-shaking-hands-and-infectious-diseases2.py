N, K, P, T = map(int, input().split())
hands=[] #입력받은거 저장
ans=[0]*(N+1) #감염 결과 저장
cnt=[0]*(N+1) #감염 횟수 저장

class Hand:
    def __init__(self,t,x,y):
        self.t=t
        self.x=x
        self.y=y


for _ in range(T):
    t, x, y = map(int, input().split())
    hands.append(Hand(t, x, y))
hands.sort(key=lambda x:x.t)
ans[P]=1
for h in hands:
    x,y=h.x,h.y
    if ans[x]==1 and cnt[x]<K:
        if not ans[y]:
            ans[y]=1
        cnt[x]+=1
    if ans[y]==1 and cnt[y]<K:
        if not ans[x]:
            ans[x]=1
        cnt[y]+=1

for i in range (1,N+1):
    print(ans[i],end="")