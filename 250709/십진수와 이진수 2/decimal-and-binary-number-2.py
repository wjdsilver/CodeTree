N = list(input())
num=0
arr=[]

for i in range(len(N)):
    num = num * 2 + int(N[i])

num*=17

while True:
    if num<2:
        arr.append(num)
        break
    arr.append(num%2)
    num//=2

for elem in arr[::-1]:
    print(elem,end="")