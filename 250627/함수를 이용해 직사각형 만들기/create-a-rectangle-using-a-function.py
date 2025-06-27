n, m = map(int, input().split())

def printstar(n,m):
    for _ in range(n):
        for _ in range(m):
            print("1",end="")
        print()

printstar(n,m)
