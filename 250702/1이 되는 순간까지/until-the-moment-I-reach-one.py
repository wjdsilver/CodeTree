N = int(input())

def recursive(m):
    if m == 1:
        return 0
    if m % 2 == 0:
        return recursive(m // 2) + 1
    else:
        return recursive(m // 3) + 1

print(recursive(N))