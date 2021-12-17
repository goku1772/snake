from turtle import Turtle

Aliment = "center"
Font = ("Courier", 10, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.s = 0
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(0,250)
        self.write(arg = f"SCORE : {self.s} ", align = Aliment, font = Font )
        self.hideturtle()

    def update(self):
        self.clear()
        self.s += 1
        self.write(arg = f"SCORE : {self.s} ", align="center", font = ("Arial", 10, "normal") )

    def game_over(self):
        self.goto(0, 0)
        self.write(arg = "GAME OVER", align="center", font = ("Arial", 10, "normal") )
