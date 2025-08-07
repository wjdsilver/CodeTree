X, Y = map(int, input().split())
cnt=0

for i in range(X,Y+1):
    i=str(i)
    Palindrome=True
    for j in range(len(i)//2):
        if i[j]==i[len(i)-1-j]:
            continue
        else:
            Palindrome=False
    if Palindrome==True:
        cnt+=1
print(cnt)