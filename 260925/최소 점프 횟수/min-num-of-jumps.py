n = int(input())
num = list(map(int, input().split())) #각 값은 해당 위치로부터의 최대 점프 거리를 의미함
answer=1000

def jump(x,count):
    global answer
    for i in range(1,num[x]+1):
        if x+i==n-1:#n번째 위치 도달
            count+=1
            answer=min(count,answer)
            return
        jump(x+i,count+1)

jump(0,0)
if answer==1000:
    print(-1)
else:
    print(answer)