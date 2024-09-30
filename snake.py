from turtle import Turtle

BODY_PART_LEN = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
X_LIM = 390
Y_LIM  = 390

class Snake:

    def __init__(self):
        self.snake_body = []
        self.createsnake()
        self.head = self.snake_body[0]

    def createsnake(self):
    # create the three initial body parts of the snake
        for bodyPart in range(3):
            self.snake_body.append(Turtle(shape="square"))
            self.snake_body[-1].color('white')
            self.snake_body[-1].penup()
            self.snake_body[-1].speed("fastest")
            self.snake_body[-1].goto(-bodyPart * BODY_PART_LEN, 0)


    def move(self):
        bp_last_index = len(self.snake_body) - 1
        # make each body part take the position of its previous body part
        for bpIndex in range(bp_last_index, 0, -1):
            previous_bp_pos_x ,previous_bp_pos_y = self.snake_body[bpIndex - 1].xcor(), self.snake_body[bpIndex - 1].ycor()
            self.snake_body[bpIndex].goto(previous_bp_pos_x ,previous_bp_pos_y)
        self.head.fd(BODY_PART_LEN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def ate(self, food):
        return self.head.distance(food) < 15

    def growtail(self):
        self.snake_body.append(Turtle(shape="square"))
        self.snake_body[-1].color('white')
        self.snake_body[-1].penup()
        self.snake_body[-1].speed("fastest")
        tail_x,tail_y = self.snake_body[-2].xcor(), self.snake_body[-2].ycor()
        self.snake_body[-1].goto(tail_x, tail_y)

    def wallcollision(self):
        return abs(self.head.xcor()) > X_LIM or abs(self.head.ycor()) > Y_LIM

    def bit_itself(self):
        for bodyPart in self.snake_body[1:]:
            if self.head.distance(bodyPart) < BODY_PART_LEN - 5:
                return True
        return False

    def reset(self):
        for bodyPart in self.snake_body:
            bodyPart.goto(1000,1000)
        self.snake_body.clear()
        self.createsnake()
        self.head = self.snake_body[0]




