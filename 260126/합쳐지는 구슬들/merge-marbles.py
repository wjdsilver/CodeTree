n, m, t = map(int, input().split())

r = []
c = []
dr = [] #방향(상하)
dc = [] #방향(좌우)
w = [] #무게

def inRange(x,y,n):
    return 0<=x<n and 0<=y<n

for _ in range(m):
        ri, ci, di, wi = input().split()
        r.append(int(ri) - 1)
        c.append(int(ci) - 1)
        w.append(int(wi))

        if di == "U":
            dr.append(-1); dc.append(0)
        elif di == "D":
            dr.append(1); dc.append(0)
        elif di == "L":
            dr.append(0); dc.append(-1)
        elif di == "R":
            dr.append(0); dc.append(1)

#1초 동안 모든 구슬 이동
def test():
    #구슬에 대하여
    for x in range(len(r)):
        nr = r[x] + dr[x]
        nc = c[x] + dc[x]
        if inRange(nr,nc,n):
            r[x]=nr
            c[x]=nc
        if not inRange(nr,nc,n):
            dr[x] *= -1
            dc[x] *= -1

    # 좌표별로 모으기
    pos={}
    for i in range(len(r)):
        p = (r[i], c[i])
        if p not in pos:
            pos[p] = []
        pos[p].append(i)

    remove = set()

    # 충돌 처리
    for group in pos.values():
        if len(group) >= 2:
            winner = group[0]
            for i in group[1:]:
                if w[i] > w[winner]:
                    winner = i

            total = 0
            for i in group:
                total += w[i]

            w[winner] = total

            for i in group:
                if i != winner:
                    remove.add(i)


    r[:]  = [r[i] for i in range(len(r)) if i not in remove]
    c[:]  = [c[i] for i in range(len(c)) if i not in remove]
    dr[:] = [dr[i] for i in range(len(dr)) if i not in remove]
    dc[:] = [dc[i] for i in range(len(dc)) if i not in remove]
    w[:]  = [w[i] for i in range(len(w)) if i not in remove]





for _ in range(t):
    test()
print(len(r),max(w))
