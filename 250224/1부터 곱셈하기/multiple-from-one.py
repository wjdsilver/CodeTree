n=int(input())
multi=1
for i in range(1,11):
    multi*=i
    if multi>=n:
        print(i)
        break
