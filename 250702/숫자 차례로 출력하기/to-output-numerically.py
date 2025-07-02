n = int(input())

def countDown(n):
    if n == 0:
        return
    print(n, end=" ")
    countDown(n - 1)
    
def countUp(n):
    if n == 0:
        return
    countUp(n - 1)
    print(n, end=" ")


countUp(n)
print()
countDown(n)