n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

str.sort()
print(str[k])