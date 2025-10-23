A = input()
ans=len(A)*2

def shift(A):
    A=A[-1]+A[:-1]
    return A[-1]+A[:-1]

def RLE(A):
    result=[]
    cnt=1
    for i in range(len(A)-1):
        if A[i]==A[i+1]:
            cnt+=1
            continue
        else:
            result.append(A[i])
            if 10>cnt:
                result.append(cnt)
            else:
                result.append(cnt//10)
                result.append(cnt%10)
            cnt=1
    if cnt==len(A):
        result.append(A[0])
        if 10>cnt:
            result.append(cnt)
        else:
            result.append(cnt//10)
            result.append(cnt%10)
    return len(result)

for i in range(len(A)):
    shift(A)
    ans=min(ans,RLE(A))

print(ans)
