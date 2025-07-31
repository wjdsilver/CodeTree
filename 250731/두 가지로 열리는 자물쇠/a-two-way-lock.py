N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
dial1=[0]*(N+1)
dial2=[0]*(N+1)
dial3=[0]*(N+1)
cnt1,cnt2,cnt3=0,0,0
def add_dial(dial,x):
    for y in ((x-2+N)%N,(x-1+N)%N,(x+N)%N,(x+1+N)%N,(x+2+N)%N):
        dial[y]+=1

for x in (a1,b1,c1,a2,b2,c2):
    if x==a1 or x==a2:
        add_dial(dial1,x)
    elif x==b1 or x==b2:
        add_dial(dial2,x)
    elif x==c1 or x==c2:
        add_dial(dial3,x)
    
for i in (dial1):
    if i==2:
        cnt1+=1
for i in (dial2):
    if i==2:
        cnt2+=1
for i in (dial3):
    if i==2:
        cnt3+=1
for j in (cnt1,cnt2,cnt3):
    if j==0:
        j=1
print(5**3*2-cnt1*cnt2*cnt3)



