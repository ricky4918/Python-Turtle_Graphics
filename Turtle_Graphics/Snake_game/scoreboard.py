from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 25, "normal")
class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.update_scoreboard()
    

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align= ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align= ALIGNMENT, font=FONT)