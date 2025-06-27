a=""
cnt=0
arr=[]
while a!="0":
    a=input()
    if cnt%2==0:
        arr.append(a)
    cnt+=1
print(cnt-1)
for i in arr:
    print(i)
