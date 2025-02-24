total=0
cnt=0
while True:
    n=int(input())
    
    if 20<=n and n<30:
        total+=n
        cnt+=1
    else:
        print(f"{total/cnt:.2f}")
        break