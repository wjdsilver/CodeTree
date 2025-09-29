n = int(input())
sequence = list(map(int, input().split()))
cnt=0

for i in range(0,n-1):
    if sequence[i:]==sorted(sequence[i:]):
        continue
    else:
        cnt+=1
    
print(cnt)