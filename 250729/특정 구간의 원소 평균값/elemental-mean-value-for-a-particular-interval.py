n = int(input())
arr = list(map(int, input().split()))

cnt=0

for i in range(n):
    for j in range(i, n):
        sum_val = 0
        for k in range(i, j + 1):
            sum_val += arr[k]
        
        av_sum=sum_val/(j-i+1)
        for k in range(i, j + 1):
            if av_sum==arr[k]:
                cnt+=1
                break

print(cnt)

