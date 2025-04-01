n=int(input())
cnt=2

for i in range(n):
    if i%2==0:
        cnt-=1
        for j in range(n):
            print(cnt,end=" ")
            cnt+=1
    else:
        cnt+=1
        for j in range(n):
            print(cnt,end=" ")
            cnt+=2
    print()