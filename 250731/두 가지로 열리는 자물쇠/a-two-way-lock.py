N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
dial1=[]
dial2=[]
dial3=[]

for i in range(N):
    dial1.append(i)
    dial2.append(i)
    dial3.append(i)

def del_dial(dial,x):
    for y in ((x-2+N)%N,(x-1+N)%N,(x+N)%N,(x+1+N)%N,(x+2+N)%N):
        if y in dial:
            dial.remove(y)
        else:
            continue

for x in (a1,b1,c1,a2,b2,c2):
    if x==a1 or x==a2:
        del_dial(dial1,x)
    elif x==b1 or x==b2:
        del_dial(dial2,x)
    elif x==c1 or x==c2:
        del_dial(dial3,x)

print(5**3*2-len(dial1)*len(dial2)*len(dial3))




