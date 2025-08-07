import sys
n = int(input())
a = list(map(int, input().split()))

fin=0
for i in range(min(a)+1,max(a)+1):
    cnt=0
    for j in range(len(a)-1):
        for k in range(j+1,len(a)):
            if a[j]!=a[k]:
                if i-a[j]==a[k]-i:
                    cnt+=1
    fin=max(cnt,fin)
print(fin)