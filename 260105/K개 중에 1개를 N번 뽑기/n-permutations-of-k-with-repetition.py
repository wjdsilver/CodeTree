K, N= map(int, input().split())

answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(curr):
    # 종료 조건
    if curr == N + 1:
        print_answer()
        return
    
    for i in range(1,K+1):#1이상 K이하 숫자
        answer.append(i)
        choose(curr + 1)
        answer.pop()
    return

choose(1)
