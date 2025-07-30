import sys
abilities = list(map(int, input().split()))
small=sys.maxsize

for i in range(4):
    for j in range(i+1,5):
        for k in range(j+1,6):
            diff=0
            diff=abs(sum(abilities)-2*(abilities[i]+abilities[j]+abilities[k]))
            small=min(small,diff)
print(small)
