N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def get_close(x):
    return [(x + i - 2 - 1) % N + 1 for i in range(5)]  # N 범위 1~N 유지

valid_combos = set()

for i in get_close(a1):
    for j in get_close(b1):
        for k in get_close(c1):
            valid_combos.add((i, j, k))

for i in get_close(a2):
    for j in get_close(b2):
        for k in get_close(c2):
            valid_combos.add((i, j, k))

print(len(valid_combos))




