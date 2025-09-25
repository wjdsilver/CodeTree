board = [list(input()) for _ in range(10)]

for i in range(10):
    if "B" in board[i]:
        br=i
    if "L" in board[i]:
        lr=i
    if "R" in board[i]:
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

if (br==lr==rr and (bc>rc>lc or bc<rc<lc)) or (bc==lc==rc and (br<rr<lr or br>rr>lr)):
    print(abs(lr-br)+abs(lc-bc)+1)
else:
    print(abs(lr-br)+abs(lc-bc)-1)