n = int(input())
arr = list(map(int, input().split()))

def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    return a*b // gcd(a,b)

def f(n):
    if n==0:
        return arr[0]
    return lcm(arr[n],f(n-1))

print(f(n-1))
