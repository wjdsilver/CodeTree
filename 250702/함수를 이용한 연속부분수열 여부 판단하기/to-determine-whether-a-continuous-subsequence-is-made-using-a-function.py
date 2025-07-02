def part(a, b):
    n, m = len(a), len(b)
    for i in range(m - n + 1):
        if b[i:i + n] == a:
            return "Yes"
    return "No"


n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(part(b,a))


