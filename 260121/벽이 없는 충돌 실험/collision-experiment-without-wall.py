#구슬의 번호와 무게 주어짐. 2초에 한칸씩 이동
#각 테스트 케이스마다 모든 구슬을 보면 시간이 너무 많이 걸림->충돌케이스만 살피기
#꼭 다시 풀어볼것

T = int(input())#총 테스트케이스

for _ in range(T): #각 테스트케이스마다
    ans=-1
    N = int(input()) #구슬 개수
    x, y, w, dr, dc, idx = [], [], [], [], [], [] #좌표, 무게, 방향

    #N개의 구슬의 좌표, 무게, 이동방향
    for i in range(N):
        xi, yi, wi, di = input().split()
        x.append(int(xi)*2)
        y.append(int(yi)*2)
        w.append(int(wi))
        idx.append(i)
        if di == "U":
            dr.append(0); dc.append(1)
        elif di == "D":
            dr.append(0); dc.append(-1)
        elif di == "L":
            dr.append(-1); dc.append(0)
        elif di == "R":
            dr.append(1); dc.append(0)


    events = []

    #세로축충돌
    U = {}
    D = {}

    for i in range(N):
        if dr[i] == 0 and dc[i] == 1:  # U
            if x[i] not in U:
                U[x[i]] = []
            U[x[i]].append(i)
        elif dr[i] == 0 and dc[i] == -1:  # D
            if x[i] not in D:
                D[x[i]] = []
            D[x[i]].append(i)

    for xx in U:
        if xx in D:
            for u in U[xx]:
                for d in D[xx]:
                    if y[u] < y[d]:
                        t = (y[d] - y[u]) // 2
                        events.append((t, u, d))

    # 가로축 충돌
    L = {}
    R = {}

    for i in range(N):
        if dr[i] == -1:  # L
            if y[i] not in L:
                L[y[i]] = []
            L[y[i]].append(i)
        elif dr[i] == 1:  # R
            if y[i] not in R:
                R[y[i]] = []
            R[y[i]].append(i)

    for yy in L:
        if yy in R:
            for l in L[yy]:
                for r in R[yy]:
                    if x[r] < x[l]:
                        t = (x[l] - x[r]) // 2
                        events.append((t, r, l))

    # 대각선 위치
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            # RU
            if dr[i] == 1 and dc[i] == 0 and dr[j] == 0 and dc[j] == 1:
                if x[i] < x[j] and y[i] > y[j] and x[j] - x[i] == y[i] - y[j]:
                    events.append((x[j] - x[i], i, j))

            # RD
            if dr[i] == 1 and dc[i] == 0 and dr[j] == 0 and dc[j] == -1:
                if x[i] < x[j] and y[i] < y[j] and x[j] - x[i] == y[j] - y[i]:
                    events.append((x[j] - x[i], i, j))

            # LU
            if dr[i] == -1 and dc[i] == 0 and dr[j] == 0 and dc[j] == 1:
                if x[i] > x[j] and y[i] > y[j] and x[i] - x[j] == y[i] - y[j]:
                    events.append((x[i] - x[j], i, j))

            # LD
            if dr[i] == -1 and dc[i] == 0 and dr[j] == 0 and dc[j] == -1:
                if x[i] > x[j] and y[i] < y[j] and x[i] - x[j] == y[j] - y[i]:
                    events.append((x[i] - x[j], i, j))

    events.sort()
    alive = [True] * N

    for t, i, j in events:
        if not alive[i] or not alive[j]:
            continue

        ans = t

        if w[i] > w[j] or (w[i] == w[j] and idx[i] > idx[j]):
            alive[j] = False
        else:
            alive[i] = False

    print(ans)