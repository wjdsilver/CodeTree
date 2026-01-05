n = int(input())

answer = []
cnt=0

def count_answer():
    global cnt
    cnt+=1

def pretty(length):
    # 종료 조건
    if length == 0:
        count_answer()
        return
    
    for i in (1,22,333,4444):
        if length>=len(str(i)):
            answer.append(i)
            pretty(length-len(str(i)))
            answer.pop()
    return

pretty(n)
print(cnt)
