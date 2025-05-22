a,b=input().split()
a=int(a)
b=int(b)
count_arr = [0] * 10
result=0

while a>1:
    left=a%b
    count_arr[left] += 1
    a=a//b

for i in count_arr:
    result+=i**2
print(result)
    