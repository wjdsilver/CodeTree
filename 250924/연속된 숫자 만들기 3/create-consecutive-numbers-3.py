a = list(map(int, input().split()))
a.sort()
s=a[0]
m=a[1]
l=a[2]
c=0

while True:
    if max(s,m,l)-min(s,m,l)!=2:#세 수가 연속되지 않았을때
        if m-s<l-m:
            s=m
            m=(m+l)//2+1
            c+=1
        else:
            l=m
            m=(m+s)//2+1
            c+=1

    else:
        print(c)
        break