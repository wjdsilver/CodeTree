arr=list(map(int, input().split()))

up=1000
down=0

for i in arr:
    if i>500:
        if i<up:
            up=i
        else:
            pass
    elif i<500:
        if i>down:
            down=i
        else:
            pass
print(down, up)