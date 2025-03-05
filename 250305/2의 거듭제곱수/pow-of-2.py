n=int(input())
cnt=0
while True:
    if n>=2:
        n//=2
        cnt+=1
    else:
        break
print(cnt)