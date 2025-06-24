n=int(input())
arr=input().split()
ans="".join(arr)
cnt=0
for i in ans:
    if cnt<5:
        print(i,end="")
        cnt+=1
    else:
        cnt=0
        print()
        print(i,end="")
        cnt+=1

    