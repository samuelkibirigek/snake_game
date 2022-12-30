from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=('Arial', 24, 'normal'))

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=('Arial', 24, 'normal'))
    def scored(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 24, 'normal'))




