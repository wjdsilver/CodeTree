x=int(input())
t = 0
left_dist = x
speed = 1

while True:
    left_dist -= speed
    t += 1

    if left_dist == 0:
        break

    if left_dist >= (speed + 1) * (speed + 2) / 2:
        speed += 1
    elif left_dist >= speed * (speed + 1) / 2:
        continue
    else:
        speed -= 1

print(t)

