score=input().split()
mid=int(score[0])
final=int(score[1])

if mid>=90:
    if final>=95:
        print(100000)
    elif final>=90:
        print(50000)
else:
    print(0)