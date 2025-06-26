word=input()
for i in range(len(word)):
    if ord("a")<=ord(word[i])<=ord("z"):
        print(chr(ord(word[i])+ord("A")-ord("a")),end="")
    elif ord("A")<=ord(word[i])<=ord("Z"):
        print(chr(ord(word[i])),end="")
    else:
        continue
