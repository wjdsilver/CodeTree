import sys

text1=input()
text2=input()
text3=input()

min=sys.maxsize
max=-sys.maxsize

if len(text1)>max:
    max=len(text1)
if len(text2)>max:
    max=len(text2)
if len(text3)>max:
    max=len(text3)

if len(text1)<min:
    min=len(text1)
if len(text2)<min:
    min=len(text2)
if len(text3)<min:
    min=len(text3)

print(max-min)