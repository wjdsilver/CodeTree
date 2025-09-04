N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]
ans=0
for i in range(1,max(num)+1):
    new_arr=[]
    for n,elem in enumerate(num):
        if elem==i:
            new_arr.append(n)
    valid = True
    for j in range(1, len(new_arr)):
        if new_arr[j] - new_arr[j-1] <= K or new_arr[j+1]-new_arr[j]<=K:
            continue
        else:
            valid=False
            break

    if valid:
        if num.count(ans)<=num.count(i):
            ans = i
        
print(ans)
        
    
    
        
