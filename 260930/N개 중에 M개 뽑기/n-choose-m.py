N, M = map(int, input().split())

answer = []

def pick_num(start, pick):
    if len(pick) == M:
        answer.append(pick[:])
        return
    if start > N:
        return 

    # start를 고르는 경우
    pick.append(start)
    pick_num(start + 1, pick)
    pick.pop()

    # start를 고르지 않는 경우
    pick_num(start + 1, pick)

pick_num(1, [])

for ans in answer:
    for num in ans:
        print(num, end=" ")
    print()
