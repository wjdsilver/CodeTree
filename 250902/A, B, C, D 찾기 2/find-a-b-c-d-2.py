nums = list(map(int, input().split()))

total=max(nums)
nums.sort()
a=nums[0]
b=nums[1]
cd=total-a-b
nums.remove(a)
nums.remove(b)
nums.remove(a+b)
c=min(nums)
d=cd-c
print(a,b,c,d)