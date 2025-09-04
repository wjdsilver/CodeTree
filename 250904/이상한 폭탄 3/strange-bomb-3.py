N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]
ans=0
for i in range(max(num)):
    new_arr=[]
    for n,elem in enumerate(num):
        if elem==i:
            new_arr.append(n)
    valid = True
    for j in range(1, len(new_arr)):
        if new_arr[j] - new_arr[j-1] > K:
            valid = False
            break

    if valid:
        if num.count(ans)<=num.count(i):
            ans = i
        
print(ans)
        
    
    
        
