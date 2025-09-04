N = int(input())
heights = [int(input()) for _ in range(N)]
fin=100000000
move=max(heights)-min(heights)-17
for i in range(move+1):
    ans=0
    for j in range(len(heights)):
        if min(heights)+i>heights[j]:
            ans+=(min(heights)+i-heights[j])**2
        elif max(heights)-move+i<heights[j]:
            ans+=(heights[j]-(max(heights)-move+i))**2
    fin=min(fin,ans)
print(fin)