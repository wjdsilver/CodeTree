n = int(input())

box=[0]*(n+1)

if n>=1:
    box[1]=1
if n>=2:
    box[2]=2
if n>=3:
    for i in range(3,n+1):
        box[i]=box[i-1]+box[i-2]

print(box[n]%10007)
