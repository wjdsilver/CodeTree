N = int(input())
watch = [
    tuple(map(int, input().split())) for _ in range(N)
]
watch.sort(key=lambda x: x[0])
curr_bird = watch[0]
cnt = 0
for i in range(1, N):
    if watch[i][0] != curr_bird[0]:
        curr_bird = watch[i]
    else:
        if watch[i][1] != curr_bird[1]:
            curr_bird = watch[i]
            cnt += 1
print(cnt)

