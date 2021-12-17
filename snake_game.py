import turtle as t
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
moving_distance = 20
up = 90
down = 270
right = 0
left = 180

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        
    def create_snake(self):
        for pos in starting_pos:
            self.add_segment(pos)

    def add_segment(self, pos):
        new = t.Turtle("square")
        new.color("white")
        new.penup()
        new.goto(pos)
        self.segment.append(new)

    def extened(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for i in range(len(self.segment)-1, 0, -1):
            x = self.segment[i-1].xcor()
            y = self.segment[i-1].ycor()
            self.segment[i].goto(x, y)
        self.head.fd(moving_distance)

    def snake_up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def snake_left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def snake_down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def snake_right(self):
        if self.head.heading() != left:
            self.head.setheading(right)


