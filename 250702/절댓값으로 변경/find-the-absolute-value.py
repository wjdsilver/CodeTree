n = int(input())
arr = list(map(int, input().split()))

def abs(n):
    if n<0:
        n=n*(-1)
    return n


for i in arr:
    print(abs(i),end=" ")