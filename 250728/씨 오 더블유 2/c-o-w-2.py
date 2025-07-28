n = int(input())
S = input()
cnt=0

for i in range(n-2):
    for j in range(i,n-1):
        for k in range(j,n):
            if S[i]=="C" and S[j]=="O" and S[k]=="W":
                cnt+=1
print(cnt)