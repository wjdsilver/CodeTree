N,M,K = map(int, input().split())
moves = list(map(int, input().split()))

answer=0
horse=[1]*K #말 위치 기록
def game(turn,point):
    global horse, answer
    #종료조건
    if turn==N:
        answer=max(answer,point)
        return 

    for i in range(K):#어떤 말을 움직일건지
            if horse[i] < M and horse[i]+moves[turn]>=M:
                horse[i]+= moves[turn]
                game(turn+1,point+1)
            else: 
                horse[i] += moves[turn]
                game(turn+1,point)
            horse[i] -= moves[turn]
game(0,0)
print(answer)
    


