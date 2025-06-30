def get_common(n, m):
    bigger = n if n >=m else m
    for i in range(bigger, n*m+1):
        if i % n == 0 and i % m ==0:
            return i

n, m = map(int, input().split())
result = get_common(n,m)
print(result)


    