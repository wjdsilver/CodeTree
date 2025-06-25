S,Q=input().split()
S=list(S)
Q=int(Q)
for i in range(Q):
    arr=input().split()
    if arr[0]=="1":
        temp=S[int(arr[1])-1]
        S[int(arr[1])-1]=S[int(arr[2])-1]
        S[int(arr[2])-1]=temp
        print("".join(S))
    elif arr[0]=="2":
        for i in range(len(S)):
            if S[i]==arr[1]:
                S[i]=arr[2]
        print("".join(S))