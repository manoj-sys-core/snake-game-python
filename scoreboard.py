from turtle import Turtle
FONT = ("Courier",15,"normal")
ALIGN = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as np:
            self.high_score = int(np.read())
        self.color("white")
        self.penup()
        self.goto(x=0,y=270)
        self.fonts()
        self.hideturtle()
    def fonts(self):
        self.clear()
        self.write(f"SCORE = {self.score} High Score {self.high_score}",align=ALIGN,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.fonts()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt","w") as op:
                op.write(f"{self.high_score}")
        self.score = 0
        self.fonts()
