#동전 있는 칸을 지나가야함 3군데. 근데 작은 수부터, 해당 위치 지나가도 굳이 동전 안가져도 됨
#그냥 1번 동전에서 시작해서 3개 줍는 모든 케이스 확인하고 
#그중 가장 적은 이동을 저장하는 방식으로 하면 될거 같은데 
n = int(input())
grid = [list(input()) for _ in range(n)]
answer=1000

bynum=[None]*11 #S, 1~9, E
coin_count = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == "S":
            bynum[0] = (i, j)
        elif grid[i][j] == "E":
            bynum[10] = (i, j)
        elif grid[i][j] != ".":
            num = int(grid[i][j])
            bynum[num] = (i, j)
            coin_count += 1

def move2coin(curr,coins,distance):#출발지,주운 동전수, 여태까지 이동한 칸수
    global answer
    if coins == 3:
        r1, c1 = bynum[curr]
        r2, c2 = bynum[10]

        distance += abs(r2 - r1) + abs(c2 - c1)

        answer = min(answer, distance)
        return

    # 다음에 주울 동전 선택
    for next_coin in range(curr + 1, 10):
        if bynum[next_coin] is None:
            continue
        if bynum[curr] and bynum[next_coin]:
            r1, c1 = bynum[curr]
            r2, c2 = bynum[next_coin]

            move_distance = abs(r2 - r1) + abs(c2 - c1)

            move2coin(
                next_coin,
                coins + 1,
                distance + move_distance
            )
    return


if coin_count < 3:
    print(-1)
else:
    move2coin(0, 0, 0)
    print(answer)