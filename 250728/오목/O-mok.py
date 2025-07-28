board = [list(map(int, input().split())) for _ in range(19)]

def omokX(i,j):
    cnt=0
    color=board[i][j]
    for m in range(5):
        if board[i+m][j]==color:
            cnt+=1
    if cnt==5:
        return color,i+3,j+1
        

def omokY(i,j):
    cnt=0
    color=board[i][j]
    for m in range(5):
        if board[i][j+m]==color:
            cnt+=1
    if cnt==5:
        return color,i+1,j+3
        
def omokXY(i,j):
    cnt=0
    color=board[i][j]
    for m in range(5):
        if board[i+m][j+m]==color:
            cnt+=1
    if cnt==5:
        return color,i+3,j+3
        
def omokYX(i,j):
    cnt=0
    color=board[i][j]
    for m in range(5):
        if board[i+m][j-m]==color:
            cnt+=1
    if cnt==5:
        return color,i+3,j-1



for i in range(15):
    for j in range(15):
        if board[i][j]!=0:
            result=omokX(i,j)
            if result:
                print(result[0])
                print(result[1],result[2])
            result=omokY(i,j)
            if result:
                print(result[0])
                print(result[1],result[2])
            result=omokXY(i,j)
            if result:
                print(result[0])
                print(result[1],result[2])
            result=omokYX(i,j)
            if result:
                print(result[0])
                print(result[1],result[2])