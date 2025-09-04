N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]
ans=0
for i in range(min(num),max(num)+1):
    new_arr=[]
    for n,elem in enumerate(num):
        if elem==i:
            new_arr.append(n)

    valid = False
    for j in range(len(new_arr)):
        if j<len(new_arr)-1 and new_arr[j+1] - new_arr[j] <= K:
            valid=True
        if j>0 and new_arr[j]-new_arr[j-1]<=K:
            valid=True

            

    if valid:
        if num.count(i)>=2:
            if num.count(ans)<=num.count(i):
                ans = i
        
print(ans)
        
    
    
        
