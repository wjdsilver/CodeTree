a, b = map(int, input().split())
n = input()

num=0
arr=[]

for i in range(len(n)):
    num = num * a + int(n[i])


while True:
    if num<b:
        arr.append(num)
        break
    arr.append(num%b)
    num//=b

for elem in arr[::-1]:
    print(elem,end="")