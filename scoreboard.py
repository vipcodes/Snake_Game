from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as sc:
            self.high_score = int(sc.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score}  HighScore:{self.high_score}", align="center", font=("arial", 18, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as sc:
                sc.write(f"{self.high_score}")
        self.score = 0
        self.update()

    def increase(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("arial", 18, "normal"))
