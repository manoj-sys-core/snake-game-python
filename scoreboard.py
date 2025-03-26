from turtle import Turtle
FONT = ("Courier",15,"normal")
ALIGN = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0,y=270)
        self.fonts()
        self.hideturtle()
    def fonts(self):
        self.write(f"SCORE = {self.score}",align=ALIGN,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER🐍!",align=ALIGN,font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.fonts()
