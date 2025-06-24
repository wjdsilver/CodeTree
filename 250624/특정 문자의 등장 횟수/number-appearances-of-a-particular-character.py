A=input()
cnt1,cnt2=0,0

for i in range(len(A)-1):
    if A[i]=='e':
        if A[i+1]=='e' :
            cnt1+=1
        elif A[i+1]=='b':
            cnt2+=1
print(cnt1,cnt2)