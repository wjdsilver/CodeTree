cnt=0
while True:
    n=int(input())
    
    if n%2==0:
        n=n//2
        print(n)
        cnt+=1
    else:
        continue 
    if cnt>=3:      
        break
