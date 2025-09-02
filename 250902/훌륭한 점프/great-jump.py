n, k = map(int, input().split())
arr = list(map(int, input().split()))


def is_possible(x):#x가 최소인 최대값일때
    if arr[0] > x:# 시작 돌도 <= x
        return False
    available_indices = [i for i, elem in enumerate(arr) if elem <= x]

    if not available_indices or available_indices[-1] != len(arr)-1:
        return False

    for i in range(1, len(available_indices)):
        if available_indices[i] - available_indices[i - 1] > k:
            return False
    return True


minimax = max(arr)
for a in range(max(arr),1,-1):
    if is_possible(a):
        minimax = min(minimax, a)

print(minimax)