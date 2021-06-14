from turtle import Turtle

STARTING_POSITION = (0,-280)
TURTLE_MOVE = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def up(self):
        self.forward(TURTLE_MOVE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False