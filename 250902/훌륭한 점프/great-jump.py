n, k = map(int, input().split())
arr = list(map(int, input().split()))


def is_possible(x):
    available_indices = []
    for i, elem in enumerate(arr):
        if elem <= x:
            available_indices.append(i)

    arr_size = len(available_indices)
    for i in range(1, arr_size):
        dist = available_indices[i] - available_indices[i - 1]
        if dist > k:
            return False
        if arr[-1] not in available_indices:
            return False

    return True


minimax = n+1
for a in range(n,1,-1):
    if is_possible(a):
        minimax = min(minimax, a)

print(minimax)