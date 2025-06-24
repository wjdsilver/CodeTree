arr = ["apple", "banana", "grape", "blueberry", "orange"]

word=input()
cnt=0

for i in arr:
    if i[2]==word or i[3] == word:
        print(i)
        cnt+=1
print(cnt)