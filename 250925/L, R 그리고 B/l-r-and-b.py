board = [list(input()) for _ in range(10)]

for i in range(10):
    if "B" in board[i]:
        br=i
    elif "L" in board[i]:
        lr=i
    elif "R" in board[i]:
        rr=i

for j in range(len(board[br])):
    if "B" in board[br][j]:
        bc=j
for j in range(len(board[lr])):
    if "L" in board[lr][j]:
        lc=j
for j in range(len(board[rr])):
    if "R" in board[rr][j]:
        rc=j

print(abs(lr-br)+abs(lc-bc)-1)