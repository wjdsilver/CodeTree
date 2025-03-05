div3=0
for _ in range(5):
    n=int(input())
    if n%3!=0:
        div3=0
        break
    elif n%3==0:
        div3=1
print(div3)