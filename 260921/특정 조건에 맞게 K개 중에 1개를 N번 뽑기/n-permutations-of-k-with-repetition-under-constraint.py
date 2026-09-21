K, N = map(int, input().split())

result = []

def dfs(sequence):
    # N개의 숫자를 모두 골랐다면 출력
    if len(sequence) == N:
        print(*sequence)
        return

    for num in range(1, K + 1):
        # 마지막 2개와 같은 숫자라면 3번 연속이 되므로 제외
        if len(sequence) >= 2 and sequence[-1] == num and sequence[-2] == num:
            continue

        sequence.append(num)
        dfs(sequence)
        sequence.pop()

dfs([])