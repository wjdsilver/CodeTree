n=int(input())
arr = list(map(int, input().split()))
temp=[]
for i in arr:
    if i%2==0:
        temp.append(i)
    else:
        pass

reversed_arr=temp[::-1]
for j in reversed_arr:
    print(j,end=" ")
    