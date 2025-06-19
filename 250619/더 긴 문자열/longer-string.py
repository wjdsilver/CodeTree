text1,text2=input().split()
if len(text1)>len(text2):
    print(text1,len(text1))
elif len(text1)<len(text2):
    print(text2,len(text2))
else:
    print("same")