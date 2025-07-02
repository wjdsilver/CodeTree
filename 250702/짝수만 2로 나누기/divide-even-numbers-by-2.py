n = int(input())
arr = list(map(int, input().split()))

def changeto2(n):
    for i in range(n):
        if arr[i]%2==0:
            arr[i]=arr[i]//2

changeto2(n)
for elem in arr:
    print(elem,end=" ")