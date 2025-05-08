n=int(input())
cnt=0
arr=[]

for i in range (1,11):
    if cnt==2:
        break
    else:
        if n*i%5==0:
            arr.append(n*i)
            cnt+=1
        else:
            arr.append(n*i)

for i in range (len(arr)):
    print(arr[i],end=" ")