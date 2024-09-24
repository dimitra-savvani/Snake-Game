from turtle import Turtle
ALIGNMENT = "center"
SCORE_FONT = ('Arial', 16, 'normal')
GAME_OVER_FONT = ('Arial', 36, 'normal')
SCORE_SCREEN_POS = (0, 370)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(SCORE_SCREEN_POS)
        self.score = 0
        self.write(f"Score: {self.score}", move = False, align=ALIGNMENT, font= SCORE_FONT)


    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move = False, align=ALIGNMENT, font= SCORE_FONT)

    def game_over(self):
        self.goto(0, 0 )
        self.write(f"GAME OVER!!!", move = False, align=ALIGNMENT, font= GAME_OVER_FONT)

