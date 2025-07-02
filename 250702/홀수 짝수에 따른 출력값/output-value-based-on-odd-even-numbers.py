N = int(input())

def ans(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    return n+ans(n-2)


print(ans(N))