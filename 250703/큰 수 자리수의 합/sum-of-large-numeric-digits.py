a, b, c = map(int, input().split())

def total(n):
    if n < 10:
        return n
    return total(n//10)+n%10

n=a*b*c
print(total(n))
