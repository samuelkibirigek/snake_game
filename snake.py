
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_STEPS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.snake_segments.append(new_segment)

    def move(self):
        for seg in range(len(self.snake_segments) - 1, 0, -1):
            x_position = self.snake_segments[seg - 1].xcor()
            y_position = self.snake_segments[seg - 1].ycor()
            self.snake_segments[seg].goto(x=x_position, y=y_position)

        self.head.forward(SNAKE_STEPS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
