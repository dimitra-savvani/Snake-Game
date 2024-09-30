from turtle import Turtle
ALIGNMENT = "center"
SCORE_FONT = ('Arial', 16, 'normal')
GAME_OVER_FONT = ('Arial', 36, 'normal')
RESET_FONT = ('Arial', 26, 'normal')
SCORE_SCREEN_POS = (0, 370)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_highscore()
        self.create()

    def create(self):
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(SCORE_SCREEN_POS)
        self.write(f"Score: {self.score}        Highscore: {self.high_score}", move = False, align=ALIGNMENT, font= SCORE_FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}        Highscore: {self.high_score}", move = False, align=ALIGNMENT, font= SCORE_FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_highscore()
        self.score = -1
        self.update()

    def read_highscore(self):
        with open('highscore.json', 'r') as file:
            return int(file.read())

    def write_highscore(self):
        with open('highscore.json', 'w') as file:
            file.write(str(self.high_score))

