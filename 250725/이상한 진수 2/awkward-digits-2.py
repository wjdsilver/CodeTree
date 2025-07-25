a = input()
na=""
ans=0
cnt=0
while cnt<1:
    for i in range(1,len(a)):
        if a[i]=="0":
            na=a[:i]+"1"+a[i+1:]
            cnt+=1
            break
    if cnt==0:
        na=a[:len(a)-1]+"0"
        break

print(int(na,2))