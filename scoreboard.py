from turtle import Turtle

ALIGN = "center"
FONT = ("aerial",16,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-250,250)
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align=ALIGN, font=FONT)

    def calculate_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGN, font=FONT)