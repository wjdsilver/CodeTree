n = int(input())
sequence = list(map(int, input().split()))
cnt=0

for i in range(0,n-1):
    if sequence[i:] is not sorted:
        cnt+=1
    
print(cnt)