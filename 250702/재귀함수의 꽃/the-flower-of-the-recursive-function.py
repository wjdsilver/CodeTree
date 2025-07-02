N = int(input())

def result(n):
    if n==0:
        return 
    print(n,end=" ")
    result(n-1)
    print(n,end=" ")

result(N)