from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 20, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.scoreboard = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.scoreboard}",
                   True, align=ALIGN,
                   font=FONT)

    def addscore(self):
        self.scoreboard += 1
        self.clear()
        self.goto(0, 270)
        self.update_score()

    def game_over(self):
        self.home()
        self.write('Game over',
                   True, align=ALIGN,
                   font=FONT)
