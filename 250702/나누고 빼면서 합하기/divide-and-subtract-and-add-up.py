n, m = map(int, input().split())
A = list(map(int, input().split()))
ans=0

def func(m):
    global ans
    while True:
        if m==1:
            ans+=A[1]
            break
        elif m%2==1:
            m-=1
            ans+=A[m]
        elif m%2==0:
            m//=2
            ans+=A[m]

func(m)
print(ans)
