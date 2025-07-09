N, B = map(int, input().split())
arr=[]

while True:
    if N<B:
        arr.append(N)
        break
    arr.append(N%B)
    N//=B

for elem in arr[::-1]:
    print(elem,end="")