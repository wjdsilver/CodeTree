R, C = map(int, input().split())
arr = [list(input().split()) for _ in range(R)]
cnt=0
if arr[0][0]!=arr[R-1][C-1]:
    for i in range(1,R-2):
        for j in range(1,C-2):
            for k in range(i + 1, R-1):
                for l in range(j + 1,C-1):
                    if arr[0][0]=="W":
                        if arr[i][j]=="B" and arr[k][l]=="W":
                            cnt+=1
                    elif arr[0][0]=="B":
                        if arr[i][j]=="W" and arr[k][l]=="B":
                            cnt+=1
                        
print(cnt)