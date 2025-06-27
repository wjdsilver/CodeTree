cnt=0
arr=[]
while True:
    word=input()
    if word=="0":
        break
    else:
        if cnt%2==0:
            arr.append(word)
        cnt+=1
print(cnt)
for i in arr:
    print(i)
