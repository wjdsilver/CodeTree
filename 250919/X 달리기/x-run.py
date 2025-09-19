X = int(input())
L = 0
t = 0

speed=1
while X//2>=L:
    L+=speed
    speed+=1
    t+=1
print(2*t)