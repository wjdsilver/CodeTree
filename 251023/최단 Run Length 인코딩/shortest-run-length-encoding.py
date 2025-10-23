A = input()
ans=len(A)*2

def shift(y):
    return y[-1]+y[:-1]
    

def RLE(x):
    result = []
    cnt = 1
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            cnt += 1
        else:
            result.append(x[i])
            result.append(str(cnt))
            cnt = 1
    result.append(x[-1])
    result.append(str(cnt))
    return len(''.join(result))

for i in range(len(A)+1):
    A=shift(A)
    ans=min(ans,RLE(A))

print(ans)
