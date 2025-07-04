unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class Bomb:
    def __init__(self,code,color,sec):
        self.code=code
        self.color=color
        self.sec=sec

bomb1=Bomb(unlock_code,wire_color,seconds)

print(f"""code : {bomb1.code}
color : {bomb1.color}
second : {bomb1.sec}""")