import sys

n = int(input())
nums = list(map(int, input().split()))
ans=[]
big=-1
for i in nums:
    if nums.count(i)==1:
        ans.append(i)
    else:
        pass
for i in ans:
    if i>big:
        big=i

print(big)
        


