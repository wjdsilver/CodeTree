X = int(input())
S = 1#속도
L = 1#이동한거리
t = 1#이동한 시간

while True:
    if X>L:
        if X//2>L:
            S+=1
        elif X//2<L:
            if S>1:
                S-=1
        L+=S
        t+=1
    elif X==L:
        print(t)
        break