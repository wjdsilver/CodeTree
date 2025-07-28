board = [list(map(int, input().split())) for _ in range(19)]
found=False

def omokX(i,j):
    cnt=0
    color=board[i][j]
    for m in range(5):
        if i<15:
            if board[i+m][j]==color:
                cnt+=1
    if cnt==5:
        return color,i+3,j+1
        

def omokY(i,j):
    cnt=0
    color=board[i][j]
    for m in range(5):
        if j<15:
            if board[i][j+m]==color:
                cnt+=1
    if cnt==5:
        return color,i+1,j+3
        
def omokXY(i,j):
    cnt=0
    color=board[i][j]
    for m in range(5):
        if i<15 and j<15:
            if board[i+m][j+m]==color:
                cnt+=1
    if cnt==5:
        return color,i+3,j+3
        
def omokYX(i,j):
    cnt=0
    color=board[i][j]
    for m in range(5):
        if i<15:
            if board[i+m][j-m]==color:
                cnt+=1
    if cnt==5:
        return color,i+3,j-1



for i in range(19):
    for j in range(19):
        if board[i][j]!=0:
            result=omokX(i,j)
            if result:
                found=True
                print(result[0])
                print(result[1],result[2])
            result=omokY(i,j)
            if result:
                found=True
                print(result[0])
                print(result[1],result[2])
            result=omokXY(i,j)
            if result:
                found=True
                print(result[0])
                print(result[1],result[2])
            result=omokYX(i,j)
            if result:
                found=True
                print(result[0])
                print(result[1],result[2])
if not found:
    print(0)