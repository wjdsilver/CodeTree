N = int(input())

def hap(n):
    if n == 0:
        return 0

    return hap(n - 1) + n


print(hap(N))