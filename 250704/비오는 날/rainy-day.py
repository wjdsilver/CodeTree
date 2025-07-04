n = int(input())
date = []
day = []
weather = []
future=[]
cnt=0

class Days:
    def __init__(self,date,day,weather):
        self.date=date
        self.day=day
        self.weather=weather
        
for _ in range(n):
    d, dy, w = input().split()
    if w=="Rain":
        date.append(d)
        day.append(dy)
        weather.append(w)
        future.append(Days(d,dy,w))
        cnt+=1

date.sort()

for i in range(cnt):
    if future[i].date==date[0]:
        print(future[i].date, future[i].day, future[i].weather)