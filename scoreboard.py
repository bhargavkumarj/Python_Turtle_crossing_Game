from turtle import Screen,Turtle
screen=Screen()
screen.title("Bhargavs Turtle v/s Cars Game")
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.update_scoreboard()
        #self.write(f"Level:{self.level}",align="left",font=FONT)
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level}",align="left",font=FONT)


    def increase_level(self):
        self.level+=1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)
