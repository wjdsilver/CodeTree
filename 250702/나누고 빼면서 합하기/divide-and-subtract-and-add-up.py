n, m = map(int, input().split())
A = [0]+list(map(int, input().split()))
ans=0

def func(m):
    global ans
    while True:
        if m==1:
            ans+=A[1]
            break
        elif m%2==1:
            ans+=A[m]
            m-=1
        elif m%2==0:
            ans+=A[m]
            m//=2

func(m)
print(ans)
