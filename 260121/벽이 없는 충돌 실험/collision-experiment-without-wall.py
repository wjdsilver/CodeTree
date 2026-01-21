#구슬의 번호와 무게 주어짐. 2초에 한칸씩 이동
T = int(input())#총 테스트케이스

for _ in range(T): #각 테스트케이스마다
    t=0
    ans=-1
    winner =0
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

    for _ in range(4000):
        if len(x) <= 1:
            break
        #모든 구슬 이동
        for i in range(len(x)):
            x[i]+=dr[i]
            y[i]+=dc[i]
        pos=[(x[i],y[i])for i in range(len(x))]
        t+=1
        #지울거 목록
        to_remove = set() 
        pos_dict = {}
        for i in range(len(x)):
            if pos[i] not in pos_dict:
                pos_dict[pos[i]] = []
            pos_dict[pos[i]].append(i)
        for group in pos_dict.values(): 
            if len(group) >= 2: 
                ans = t 
                winner = group[0] 
                for i in group[1:]: 
                    if w[i] > w[winner] or (w[i] == w[winner] and idx[i] > idx[winner]): 
                        winner = i 
                for i in group: 
                    if i != winner:
                        to_remove.add(i)

        alive = [i for i in range(len(x)) if i not in to_remove]

        x  = [x[i] for i in alive]
        y  = [y[i] for i in alive]
        w  = [w[i] for i in alive]
        dr = [dr[i] for i in alive]
        dc = [dc[i] for i in alive]
        idx = [idx[i] for i in alive]
    

    print(ans)