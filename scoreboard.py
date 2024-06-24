from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Comic Sans MS", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        self.game_is_on = True

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def endgame(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
        self.game_is_on = False

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
