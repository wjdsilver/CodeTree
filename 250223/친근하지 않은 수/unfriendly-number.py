n=int(input())
cnt=0
for i in range (1,n+1):
    if i%2!=0:
        if i%3!=0:
            if i%5!=0:
                cnt+=1
print(cnt)