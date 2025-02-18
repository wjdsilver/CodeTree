n=int(input())
room=0
hall=0
wc=0
for i in range(1,n+1):
    if i%12==0:
        wc+=1
    elif i%3==0:
        hall+=1
    elif i%2==0:
        room+=1
print(room,hall,wc)
