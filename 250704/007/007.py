secret_code, meeting_point, time = input().split()
time = int(time)

class Secret:
    def __init__(self,code,place,time):
        self.code=code
        self.place=place
        self.time=time

S1=Secret(secret_code, meeting_point, time)
print(f"""secret code : {S1.code}
meeting point : {S1.place}
time : {S1.time}""")
