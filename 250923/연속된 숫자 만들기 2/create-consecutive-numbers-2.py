pos = list(map(int, input().split()))

if max(pos)-min(pos)!=2:#연속이 아닐때
    if  abs(pos[0]-pos[1])==1 or abs(pos[1]-pos[2])==1 or abs(pos[0]-pos[2])==1:
        print(1)
    else:
        print(2)
else:
    print(0)