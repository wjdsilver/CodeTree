inp = [list(map(int, list(input().strip()))) for _ in range(3)]
cnt=0

for i in range(1,10):
    for j in range(1,10):
        if i!=j:
            TTT=False
            for n in range(3):
                if inp[n][0]==i:
                    if inp[n][1]==i and inp[n][2]==j:
                        TTT=True
                    elif inp[n][1]==j:
                        if inp[n][2]==i or inp[n][2]==j:
                            TTT=True
            for n in range(3):
                if inp[0][n]==i:
                    if inp[1][n]==i and inp[2][n]==j:
                        TTT=True
                    elif inp[1][n]==j:
                        if inp[2][n]==i or inp[2][n]==j:
                            TTT=True
            if inp[0][0]==i:
                if inp[1][1]==i and inp[2][2]==j:
                    TTT=True
                if inp[1][1]==j:
                    if inp[2][2]==i or inp[2][2]==j:
                        TTT=True
            if inp[0][2]==i:
                if inp[1][1]==i and inp[2][0]==j:
                    TTT=True
                if inp[1][1]==j:
                    if inp[2][0]==i or inp[2][0]==j:
                        TTT=True
            if TTT==True:
                cnt+=1
print(cnt)
