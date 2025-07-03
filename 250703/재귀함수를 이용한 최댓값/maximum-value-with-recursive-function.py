n = int(input())
arr = list(map(int, input().split()))

def f(n):
    if n==0:
        return arr[0]
    elif n==1:
        return arr[1]
    return max(f(n-2),arr[n-1])

print(f(n))